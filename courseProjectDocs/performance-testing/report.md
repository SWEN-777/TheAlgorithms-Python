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

## Stress Test

**Test Scope and Design:**
We tested the core efficiency and time complexity of the Doubly Linked List implementation under a single-threaded sequential load, specifically focusing on the performance of O(1) vs. O(N) operations.

**Configuration:**
- Sequential, single-threaded execution.
- Total Operations: 25,000 (10,000 insertions, 10,000 searches, 5,000 deletions).

**Results:**
| Operation Type                 | Total Count | Inferred Time Complexity      | Time Taken (s) |
|-------------------------------|-------------|-------------------------------|----------------|
| Insertion Stress (Head)       | 10,000      | O(N) (Expected O(1))          | 5.51           |
| Search Stress (Linear Traversal) | 10,000   | O(N) (Expected O(N))          | 7.31           |
| Deletion Stress (Mixed Index) | 5,000       | O(N²) (Expected O(N))         | 10.58          |
| Total Test Duration           | 25,000      | N/A                           | ~23.4          |


**Findings:**
The high duration and complexity violations are attributed to the __len__ method calculating the list's size by traversing the entire list (O(N)) instead of using an O(1) size counter. Since methods like delete_at_nth call len() inside a loop, the test rapidly created the observed O(N^2) slowdown.

---

## Group Contributions
- Uzair Mukadam: Designed and ran Spike Test, documented results.
- Shridhar Vilas Shinde: Designed and ran Load Test, documented results.
- Rohini: Designed and ran Stress Test, documented results.
