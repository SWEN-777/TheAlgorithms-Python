import time
import random
import psutil
import os
from data_structures.hashing.quadratic_probing import QuadraticProbing

def spike_test():
    qp = QuadraticProbing(10)  # start small to force rehashing
    num_operations = 100000    # total insertions
    spike_size = 20000         # sudden surge

    # Baseline load
    print("Running baseline load...")
    start = time.time()
    for i in range(num_operations - spike_size):
        qp.insert_data(random.randint(0, 100000))
    baseline_duration = time.time() - start
    print(f"Baseline duration: {baseline_duration:.2f}s")

    # Spike load
    print("Running spike load...")
    start = time.time()
    for i in range(spike_size):
        qp.insert_data(random.randint(0, 100000))
    spike_duration = time.time() - start
    print(f"Spike duration: {spike_duration:.2f}s")

    # Collect system metrics
    process = psutil.Process(os.getpid())
    cpu_usage = process.cpu_percent(interval=1)
    mem_usage = process.memory_info().rss / (1024 * 1024)

    print(f"CPU usage: {cpu_usage}%")
    print(f"Memory usage: {mem_usage:.2f} MB")

if __name__ == "__main__":
    spike_test()
