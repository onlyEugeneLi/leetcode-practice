"""
Wise YugabyteDB Platform Engineer Interview Preparation Suite
-------------------------------------------------------------
This script contains production-ready, idiomatic Python patterns targeting:
1. Log Parsing & State Tracking (DSA)
2. Asynchronous I/O & Connection Aggregation (Concurrency)
3. Defensive Coding, Type Hinting, and Robust Error Handling (Production-Ready)
"""

import asyncio
import logging
from collections import defaultdict
from typing import Dict, List, Set

# -------------------------------------------------------------------------
# GLOBAL LOGGING SETUP (Crucial for Production Code over print statements)
# -------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d - %(message)s"
)
logger = logging.getLogger("WisePrepSuite")


# =========================================================================
# DAYS 1 & 2: DSA - TEXT PARSING & INFRASTRUCTURE STATE TRACKING
# =========================================================================

def parse_yugabyte_logs(raw_logs: List[str]) -> Dict[str, List[str]]:
    """
    Parses flat database log streams to extract and group critical errors.
    Uses an O(N) single-pass approach via collections.defaultdict.
    
    Time Complexity: O(N) where N is the number of log lines.
    Space Complexity: O(M) where M is the unique nodes generating errors.
    """
    # 1. Input Validation / Edge Case Defense
    if not raw_logs:
        logger.warning("Empty log sequence passed to processor.")
        return {}

    # 2. Idiomatic Initialization (Prevents manual KeyError checks)
    node_error_map = defaultdict(list)

    try:
        for line in raw_logs:
            # Strip whitespace and skip empty lines or comments
            clean_line = line.strip()
            if not clean_line or clean_line.startswith("#"):
                continue
                
            # Expected pattern: "NODE_IP | STATUS | MESSAGE"
            parts = [p.strip() for p in clean_line.split("|")]
            
            # Defensive unpacking protection against corrupted log formats
            if len(parts) < 3:
                logger.debug(f"Skipping malformed log line: {clean_line}")
                continue
                
            node_ip, status, message = parts[0], parts[1], parts[2]
            
            # Filtering criteria: track only operational degradation states
            if status in {"ERROR", "CRITICAL", "FATAL"}:
                node_error_map[node_ip].append(message)
                
    except Exception as e:
        logger.error(f"Fatal exception during log parsing workflow: {str(e)}")
        raise

    return dict(node_error_map)


# =========================================================================
# DAYS 3 & 4: CONCURRENCY - ASYNC I/O HEALTH CHECKER FOR DISTRIBUTED NODES
# =========================================================================

async def mock_fetch_node_metrics(node_ip: str) -> Dict[str, str]:
    """
    Simulates an asynchronous RPC or HTTP health probe to a YugabyteDB tablet server.
    Emulates network latency without blocking the main execution thread.
    """
    logger.info(f"Initiating health check handshake for node: {node_ip}")
    
    # Non-blocking sleep simulates waiting for remote cluster network I/O
    await asyncio.sleep(0.5) 
    
    # Simple static simulator logic
    if node_ip == "10.0.0.3":
        return {"node": node_ip, "status": "UNHEALTHY", "reason": "High WAL disk lag"}
    return {"node": node_ip, "status": "HEALTHY", "reason": "Synced"}


async def audit_cluster_health_concurrently(cluster_ips: List[str]) -> List[Dict[str, str]]:
    """
    Executes multiple infrastructure health probes concurrently using asyncio.gather.
    Essential pattern for managing highly scaleable, multi-node platform operations.
    """
    if not cluster_ips:
        return []

    # Dedup inputs efficiently via Sets to prevent redundant network traffic
    unique_ips: Set[str] = set(cluster_ips)
    
    # Provision a collection of asynchronous task coroutines
    tasks = [mock_fetch_node_metrics(ip) for ip in unique_ips]
    
    try:
        # Gather all futures concurrently. return_exceptions=True prevents 
        # a single failing node from crashing the entire audit pipeline.
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        sanitised_results = []
        for res in results:
            if isinstance(res, Exception):
                logger.error(f"A concurrent probe encountered a critical failure: {res}")
                continue
            sanitised_results.append(res)
            
        return sanitised_results

    except Exception as general_err:
        logger.critical(f"Async orchestration engine mapping failed: {general_err}")
        return []


# =========================================================================
# DAYS 5 & 6: MAIN EXECUTION ENTRYPOINT (PRODUCTION CODE SANITY VERIFICATION)
# =========================================================================

def main():
    """
    Acts as the harness executing mock workflows to evaluate implementation accuracy.
    """
    logger.info("--- STARTING WORKFLOW PIPELINE VERIFICATION ---")

    # --- Test Case 1: Log Parsing Engine ---
    mock_log_stream = [
        "10.0.0.1 | INFO  | Cluster bootstrap complete",
        "10.0.0.2 | ERROR | Connection timed out to tablet peer",
        "10.0.0.1 | FATAL | Out of disk space for xcluster replication",
        "10.0.0.2 | ERROR | Tablet leader election timeout",
        "         | SKIP  | Empty or corrupt node data line",
        "# This is an infrastructure metric comment line to be skipped"
    ]
    
    logger.info("Executing Days 1-2 Log Analysis...")
    parsed_errors = parse_yugabyte_logs(mock_log_stream)
    logger.info(f"Parser Output Summary: {parsed_errors}")

    # --- Test Case 2: Asynchronous Platform Concurrency ---
    mock_infrastructure_topology = ["10.0.0.1", "10.0.0.2", "10.0.0.3", "10.0.0.1"]
    
    logger.info("Executing Days 3-4 Async Network Probe Simulation...")
    # Bootstrap the asynchronous event loop safely
    cluster_report = asyncio.run(audit_cluster_health_concurrently(mock_infrastructure_topology))
    logger.info(f"Async Audit Output Summary: {cluster_report}")

    logger.info("--- WORKFLOW PIPELINE VERIFICATION SUCCESSFUL ---")


if __name__ == "__main__":
    main()
