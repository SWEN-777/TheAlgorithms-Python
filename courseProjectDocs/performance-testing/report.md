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

## Group Contributions
- Uzair Mukadam: Designed and ran Spike Test, documented results.
