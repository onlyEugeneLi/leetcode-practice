# SRE Coding Interview Prep Plan — 1 Month

## Table of Contents
- [Week 1 — Text Processing & Log Parsing](#week-1--text-processing--log-parsing-foundation)
- [Week 2 — JSON, CSV & Structured Data](#week-2--json-csv--structured-data)
- [Week 3 — System Monitoring & Process Management](#week-3--system-monitoring--process-management)
- [Week 4 — Algorithms Applied to SRE Scenarios](#week-4--algorithms-applied-to-sre-scenarios)
- [Interview Meta-Skills](#interview-meta-skills-practice-every-session)
- [Quick Reference: Most Common Bash Patterns](#quick-reference-most-common-bash-patterns)
- [Progress Tracker](#progress-tracker)

---

**Goal:** Be comfortable handling any practical SRE coding question in bash and Python.  
**Assumed level:** Intermediate bash (pipes, grep, basic awk) — needs more complex scenario practice.  
**Format:** One notebook per topic, numbered to match this plan.

Reference: 
- [Introduction to Linux Shell and Shell Scripting](https://www.geeksforgeeks.org/linux-unix/introduction-linux-shell-shell-scripting/)
- [Linux commands](https://www.geeksforgeeks.org/linux-unix/linux-commands/)
- [Bash Scripting Fundamentals](https://www.geeksforgeeks.org/linux-unix/bash-scripting-introduction-to-bash-and-bash-scripting/)
- [Python basics](https://www.w3schools.com/python/python_dictionaries_access.asp)

---

## Week 1 — Text Processing & Log Parsing (Foundation)

These are the most common SRE interview question types. Master them first.

### Topics
- Regex with `grep -E` and Python `re`
- Pipeline: `tr`, `sort`, `uniq -c`, `cut`, `awk`
- Parsing structured logs (nginx, syslog, CSV)
- Script safety: `set -euo pipefail` boilerplate
- `while read` loops for processing large files line-by-line without high memory usage

### Practice Problems
1. Given an nginx access log, find the top 5 IPs by request count
2. Count how many requests returned each HTTP status code (200, 404, 500, etc.)
3. Find the slowest 10 requests by response time from a log file
4. Extract all unique user agents from a log
5. Count error rate per minute over a 1-hour window

### Notebook
`2-log-parsing.ipynb`

### Key Tools
| Bash | Python |
|------|--------|
| `awk '{print $1}'` | `re.findall()` |
| `grep -E` | `collections.Counter` |
| `sort \| uniq -c \| sort -rn` | `csv.reader`, `open()` |
| `cut -d' ' -f1` | `str.split()`, list comprehensions |
| `while read line; do ...; done < file` | `for line in f:` |
| `set -euo pipefail` (script header) | N/A |

---

## Week 2 — JSON, CSV & Structured Data

SREs deal with API responses, config files, and exported metrics constantly.

### Topics
- Parse and filter JSON (nested objects, arrays)
- Transform and aggregate CSV data
- Output formatted tables or summaries
- `kubectl -o json` + `jq` for Kubernetes object inspection

### Practice Problems
1. Given a JSON array of jobs, print only the failed ones with their timestamps
2. From a CSV of server metrics, find all servers where CPU > 80%
3. Flatten a nested JSON config into key=value pairs
4. Given a JSON list of deployments, group by `status` and count each
5. Merge two CSV files on a common column (like a join)
6. Use `kubectl get pods -o json | jq` to list all pods not in `Running` state

### Notebook
`3-json-csv.ipynb`

### Key Tools
| Bash | Python |
|------|--------|
| `jq '.[] \| select(.status=="failed")'` | `json.load()` |
| `jq -r '.name'` | `csv.DictReader` |
| `kubectl get pods -o json \| jq '.items[].status.phase'` | `pandas` (if allowed) or plain dicts |

---

## Week 3 — System Monitoring & Process Management

SRE-specific: you'll be asked to write scripts that inspect or manage a running system.

### Topics
- Disk, CPU, memory usage checks
- Process inspection and filtering with `pgrep` and `ps`
- File system searches
- Alerting thresholds and retry logic
- Exit code handling: `if/else` based on command success/failure

### Practice Problems
1. Write a script that alerts if any disk partition exceeds 80% usage
2. Find the top 5 processes by memory usage
3. Find all files modified in the last 24 hours under `/var/log`
4. Kill all processes matching a given name pattern (safely — confirm before kill using `pgrep` first)
5. Write a health check script: ping a list of hosts and report which are down
6. Write a script that checks all pods in a namespace; if a pod shows `CrashLoopBackOff`, extract its last 20 log lines and restart its deployment

### Notebook
`4-system-monitoring.ipynb`

### Key Tools
| Bash | Python |
|------|--------|
| `df -h`, `du -sh` | `psutil` |
| `ps aux --sort=-%mem` | `subprocess.run()` |
| `pgrep -f <pattern>` | `pathlib`, `os.walk()` |
| `find . -mtime -1` | `socket`, `requests` |
| `ping -c 1`, `nc -z` | N/A |
| `$? / if command; then` (exit codes) | `subprocess.returncode` |

---

## Week 4 — Algorithms Applied to SRE Scenarios

Light algorithms — not LeetCode hard. Focus on real use cases.

### Topics
- Sliding window (rate limiting, moving averages)
- Deduplication and set operations
- Sorting and ranking
- Simple graph traversal (service dependency chains)
- AWS CLI automation for infrastructure management

### Practice Problems
1. Given a stream of timestamps, detect if more than 100 requests occurred in any 60-second window (rate limiting)
2. Given a list of deployment events, find services that were deployed more than 3 times in a day
3. Given a dependency map, find all services that depend (directly or transitively) on a given service
4. Deduplicate a list of alert events — keep only the first occurrence per host per hour
5. Write a script to find all unattached EBS volumes, calculate their combined size, and prompt the user before deleting (`read -p` + AWS CLI)

### Notebook
`5-algorithms-sre.ipynb`

### Key Tools
| Concept | Bash / Python |
|---------|--------------|
| Sliding window | `collections.deque` |
| Deduplication | `set`, `dict` keyed by (host, hour) |
| Graph traversal | `dict` adjacency list + BFS/DFS |
| Sorting with key | `sorted(data, key=lambda x: x['ts'])` |
| AWS resource queries | `aws ec2 describe-volumes --filters` + `jq` |
| User confirmation | `read -p "Delete? [y/N]: " confirm` |

### External Practice
- [SadServers](https://sadservers.com) — interactive Linux/SRE troubleshooting challenges, aim for 3 per week

---

## Interview Meta-Skills (Practice Every Session)

These matter as much as correctness:

1. **Clarify before coding** — ask about input format, edge cases, scale
   - "Is this a file path or a string? Could it be empty? What's the expected output format?"
2. **State your approach first** — one sentence before writing any code
3. **Offer both bash and Python** — signals versatility; bash for quick ops, Python for logic-heavy tasks
4. **Call out edge cases** — empty input, duplicate lines, malformed data, very large files
5. **Know your complexity** — for SRE questions, O(n) is almost always fine; just be able to state it

---

## Quick Reference: Most Common Bash Patterns

```bash
# Top N by frequency
awk '{print $1}' file.log | sort | uniq -c | sort -rn | head -5

# Filter by field value
awk '$9 == "500"' access.log          # HTTP 500s (field 9 in nginx log)

# Sum a column
awk '{sum += $NF} END {print sum}' file

# Find files modified in last 24h
find /var/log -mtime -1 -type f

# Check disk usage and alert
df -h | awk 'NR>1 && $5+0 > 80 {print "ALERT:", $0}'

# Top processes by memory
ps aux --sort=-%mem | head -6
```

---

## Progress Tracker

| Week | Notebook | Status |
|------|----------|--------|
| 1 | `2-log-parsing.ipynb` | [ ] Not started |
| 2 | `3-json-csv.ipynb` | [ ] Not started |
| 3 | `4-system-monitoring.ipynb` | [ ] Not started |
| 4 | `5-algorithms-sre.ipynb` | [ ] Not started |

---

## Existing Problems

| File | Topic | Status |
|------|-------|--------|
| `1-free-form-descriptor.ipynb` | Free-form descriptor filtering + word frequency | Done |
