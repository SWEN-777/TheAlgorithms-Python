import time
import random
import psutil
import os
from threading import Thread
from data_structures.trie.trie import TrieNode

def worker_task(trie, operations, results, worker_id):
    """Worker thread to simulate concurrent user operations"""
    start_time = time.time()
    for _ in range(operations):
        operation = random.choices(['insert', 'find', 'delete'], weights=[2, 3, 1])[0]
        word = random.choice(common_words)

        if operation == 'insert':
            word = word + str(random.randint(1, 1000))
            trie.insert(word)
        elif operation == 'find':
            trie.find(word)
        elif operation == 'delete':
            trie.delete(word)

    duration = time.time() - start_time
    results[worker_id] = duration

def load_test():
    # Initialize Trie with common words
    trie = TrieNode()
    trie.insert_many(common_words[:40])

    num_users = 100
    operations_per_user = 400
    total_operations = num_users * operations_per_user

    print(f"Starting load test with {num_users} concurrent users...")
    print(f"Each user will perform {operations_per_user} operations")
    print(f"Total operations: {total_operations}")
    print()

    # Track results
    results = {}
    threads = []

    # Start timing
    overall_start = time.time()

    # Create and start worker threads
    for i in range(num_users):
        thread = Thread(target=worker_task, args=(trie, operations_per_user, results, i))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    overall_duration = time.time() - overall_start

    # Calculate metrics
    throughput = total_operations / overall_duration
    avg_response_time = (sum(results.values()) / len(results)) / operations_per_user * 1000  # in ms

    # Collect system metrics
    process = psutil.Process(os.getpid())
    cpu_usage = process.cpu_percent(interval=1)
    mem_usage = process.memory_info().rss / (1024 * 1024)

    # Print results
    print(f"Load test completed in {overall_duration:.2f}s")
    print(f"Total operations: {total_operations}")
    print(f"Throughput: {throughput:.2f} req/s")
    print(f"Average response time: {avg_response_time:.2f}ms")
    print(f"CPU usage: {cpu_usage}%")
    print(f"Memory usage: {mem_usage:.2f} MB")

# Common words for testing
common_words = [
    "apple", "application", "apply", "banana", "bandana", "band",
    "cat", "catch", "category", "dog", "door", "double",
    "elephant", "element", "eleven", "fish", "fishing", "first",
    "great", "green", "group", "house", "horse", "hotel",
    "internet", "interest", "internal", "jump", "jungle", "just",
    "king", "kingdom", "kitchen", "love", "lovely", "lover",
    "mother", "mountain", "mouse", "nature", "natural", "navigate",
    "ocean", "open", "orange", "park", "party", "particle",
    "queen", "question", "quick", "rain", "rainbow", "raise",
    "sun", "sunny", "sunday", "tree", "treat", "treasure",
    "under", "universe", "up", "valley", "value", "van",
    "water", "wave", "way", "yellow", "yes", "yesterday",
    "zebra", "zero", "zone"
]

if __name__ == "__main__":
    load_test()
