# Performance Testing Instructions

## Setup
Install Locust:
```bash
pip install locust
```

## Run Spike Test
From the project root:
```bash
locust -f courseProjectDocs/performance-testing/spike_test.py
```

## Expected Output

- Spike duration showing time it took to complete the inputs

- CPU usage spike

- Memory usage spike 

## Run Load Test
From the project root:
```bash
PYTHONPATH=. python courseProjectDocs/performance-testing/load_test.py
```

## Expected Output (Load Test)

- Total operations completed

- Throughput (requests per second)

- Average response time

- CPU usage

- Memory usage

## Notes
- Spike tests simulate sudden surges of traffic, not gradual load.

- Results may vary depending on hardware.

- Optimize rehashing logic to mitigate latency spikes.