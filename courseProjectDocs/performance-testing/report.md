# Performance Testing Report

---

## Spike Test
**Test Scope and Design:**  
We tested sudden surge of insertions using Locust.  

**Configuration:**  
- 0 → 200 users in 10 seconds  
- Duration: 2 minutes  

**Results:**

- **Baseline Load:** 80k insertions completed in 64.20s  
- **Spike Load:** 20k insertions completed in 0.02s  
- **CPU Usage:** Reported as 0.0% (measurement artifact due to short spike duration)  
- **Memory Usage:** ~29.45 MB stable  

### Findings
- The spike workload completed too quickly to capture meaningful CPU metrics.  
- Memory usage remained stable, indicating efficient handling of sudden load.  
- Rehashing likely occurred during baseline, so spike inserts were faster.  
- Recommendation: Increase spike size (e.g., 100k) or measure CPU inside the loop to capture real utilization.

---

## Load Test

**Test Scope and Design:**
We tested sustained concurrent operations on Trie data structure using Python threading.

**Configuration:**
- 100 concurrent users (threads)
- 400 operations per user
- Total: 40,000 operations
- Operations: insert, find, delete with weights 2:3:1

**Results:**

- **Total Operations:** 40,000
- **Duration:** 0.06s
- **Throughput:** ~658,000 req/s
- **Response Time:** 0ms average (sub-millisecond)
- **CPU Usage:** 0.0%
- **Memory Usage:** ~16.62 MB

**Findings:**

- All Trie operations completed extremely fast with zero failures.
- High throughput achieved due to efficient in-memory operations.
- CPU usage reported as 0.0% due to very short test duration.
- The Trie handled 100 concurrent threads efficiently with no bottlenecks detected.

---

## Group Contributions
- Uzair Mukadam: Designed and ran Spike Test, documented results.
- Shridhar Vilas Shinde: Designed and ran Load Test, documented results.
