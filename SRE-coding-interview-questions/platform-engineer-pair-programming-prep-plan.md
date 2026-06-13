# 🗺️ Wise Database Platform Engineer: 7-Day HackerRank CodePair Prep Plan

This plan is tailored specifically to the **Wise Backend Pair Programming** rubric and your target **Database Platform** team.

---

## 🎯 The Wise Evaluation Criteria Matrix
To pass this 60-minute CodePair round, you must actively demonstrate these four pillars while you write code:
1. **Collaboration:** Think out loud. Treat the interviewer as a teammate. If requirements are open-ended, ask clarifying questions before typing a single line.
2. **Architecture & Clean Code:** Write clean, readable code. Adhere to **SOLID**, **DRY**, and **KISS** principles. Break your solution into small, testable, and modular functions.
3. **Language Mechanics:** Expect specific questions on Python data structure implementations, exception handling, and memory/concurrency handling.
4. **No Riddles:** Focus entirely on clean execution of computer science fundamentals, data structures (Arrays, Maps, Sets), and time/space complexity.

---

## 📅 Day-by-Day Execution Plan

### 🚀 Day 1: Python Deep Dive (Internal Implementations & Exceptions)
Wise explicitly tests your understanding of language features and data structure implementations.
*   **Study Focus:** 
    *   How are Python `dict` and `set` implemented under the hood (hash tables, collision handling, O(1) amortized lookups)?
    *   Time and space complexities of standard operations on `list`, `deque`, and `dict`.
    *   Python's memory management basics (reference counting, garbage collection).
*   **Practice Task:** Open HackerRank and solve 3–4 medium array or hashmap problems *without* using built-in shortcuts first, to ensure you can explain the underlying mechanics.

### 🏗️ Day 2: Clean Code Practices (SOLID, DRY, KISS in Python)
You will be judged heavily on *how* you write code, not just getting the right answer.
*   **Study Focus:**
    *   **KISS (Keep It Simple, Stupid):** Avoid over-engineering a highly complex algorithmic trick if a clear, readable approach exists.
    *   **DRY (Don't Repeat Yourself):** Abstract repetitive setup or validation logic into clear helper functions.
    *   **SOLID:** Ensure single responsibility for your classes and functions.
*   **Practice Task:** Take an old solution you wrote and refactor it. Focus on adding strict Type Hinting (`from typing import List, Dict`), writing clean docstrings, and handling invalid input gracefully using custom `try-except` blocks.

### 💾 Day 3: Modeling Database Configuration & Cloud Topology
Aligning with the Database Platform team's need to manage ~1,000 distributed database instances.
*   **The Scenario:** You are given an unstructured nested dictionary/JSON payload representing a distributed database cluster configuration across cloud availability zones.
*   **Practice Task:** Write a robust Python class that parses this topology configuration, validates it against business rules (e.g., ensuring a high-availability cluster has nodes spread across at least 3 zones), and implements an elegant custom exception class if validation fails.
*   **Wise Focus:** Tests clean code structure, data structures, and exception handling.

### 🔄 Day 4: State Automation & Resource Allocation Logic
Wise frequently uses practical business automation scenarios that evaluate data structures.
*   **The Scenario:** Implementing the classic **First Fit Decreasing (Bin Packing)** concept, an automation logic pattern often seen in Wise infrastructure rounds.
*   **Practice Task:** Write a Python script that takes a list of variable database backup sizes and optimally distributes/allocates them across standard storage volumes of a fixed maximum capacity.
*   **Wise Focus:** Tests algorithmic logic, array manipulation, and greedy optimization without resorting to artificial LeetCode brain-teasers.

### 🔒 Day 5: Concurrency, Network Basics, & Client-Service States
The Wise rubric advises refreshing your knowledge of microservices and basic concurrency.
*   **Study Focus:** 
    *   How Python handles concurrency (threading vs. multiprocessing vs. `asyncio`, and the role of the Global Interpreter Lock).
    *   Basic state machine logic for handling client-service communications (e.g., handling transient network retries).
*   **Practice Task:** Write an in-memory Rate Limiter class (e.g., token bucket) or a simple connection pool controller that tracks request timestamps per API client and handles boundary limits safely.

### 🗣️ Day 6: HackerRank CodePair Simulation (The "Narrative" Drill)
Wise explicitly notes: *"We're mostly interested to learn how you think so please provide a narrative as you go through the code."*
*   **Practice Task:** Choose any realistic data processing problem. Set a timer for 45 minutes. Force yourself to speak out loud continuously while coding alone.
*   **The Protocol:**
    1. Spend 5 minutes stating your assumptions and asking "mock" clarifying questions.
    2. Explain your architectural choice *before* typing.
    3. Run manual `assert` tests at the bottom of the HackerRank window to prove your code works for empty or invalid edge cases.

### 🏁 Day 7: Refactor, Polish, and Strategy Review
*   **Review:** Look over your implementations from Days 3, 4, and 5. Ensure they perfectly model the **KISS** and **DRY** principles.
*   **Mental Checklist for Interview Day:**
    *   If a requirement is intentionally open-ended, **always** stop and ask clarifying questions first.
    *   If you forget a specific syntax, don't panic. Explicitly tell the interviewer what you want to achieve, and they will gladly help you with the syntax.
    *   Treat the interviewer like an engineering peer you are collaborating with on a production ticket.

---

## 🛠️ Code Prompt to Practice Right Now
Copy this layout into HackerRank to test your structural thinking, custom error handling, and clean coding practices under the Wise rubric:

```python
from typing import List, Dict, Any

class InvalidTopologyError(Exception):
    """Raised when the infrastructure configuration violates safety rules."""
    pass

class DBClusterValidator:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        
    def validate_high_availability(self) -> bool:
        # 1. Check if nodes are empty
        # 2. Parse nodes and track distinct Availability Zones using a Set
        # 3. Raise InvalidTopologyError if rules are violated
        # 4. Return True if safe
        pass

# --- Manual Test Suite to run in HackerRank ---
if __name__ == "__main__":
    mock_payload = {
        "cluster_name": "yugabyte-prod-lon",
        "nodes": [
            {"id": "node-1", "az": "eu-west-1a"},
            {"id": "node-2", "az": "eu-west-1b"}
        ]
    }
    # Run your assertions here to demonstrate testability to your interviewer!

```