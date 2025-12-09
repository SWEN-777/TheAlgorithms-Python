import time
import random
import sys
from doubly_linked_list import DoublyLinkedList

# Set a high recursion limit 
sys.setrecursionlimit(10000)

# --- CONFIGURATION ---
NUM_OPERATIONS = 10000 
# ---------------------

def run_stress_test(num_ops: int):
    """Runs a series of stress tests on the DoublyLinkedList, avoiding 
       methods that rely on the slow O(N) __len__ function for mass ops."""
    
    print("======================================================")
    print(f"🚀 Starting Doubly Linked List Stress Test (Small Scale)")
    print(f"Total Operations per Test: {num_ops:,}")
    print("======================================================")
    
    list_to_test = DoublyLinkedList()
    
    # 1. STRESS INSERTION (Head Operations Only - O(1))
    print("\n--- TEST 1: Insertion Stress (O(1) Head Operations Only) ---")
    start_time = time.time()
    for i in range(num_ops):
        # Using insert_at_head(i) which is O(1) in your code
        list_to_test.insert_at_head(i)
    end_time = time.time()
    
    # We must call len(list_to_test) ONCE here to get the final count.
    final_insertion_count = len(list_to_test)
    
    print(f"   Total elements inserted: {final_insertion_count:,}")
    print(f"   Time taken for {num_ops:,} insertions: {end_time - start_time:.4f} seconds")
    
    # 2. STRESS SEARCH (Testing O(n) average-case complexity)
    print("\n--- TEST 2: Search Stress (O(n) Operations) ---")
    
    # Generate a list of random values to search for 
    search_values = []
    # Values inserted in Test 1 were 0 to num_ops - 1
    for _ in range(num_ops):
        if random.random() < 0.5:
            # Search for an existing element
            search_values.append(random.randint(0, num_ops - 1))
        else:
            # Search for a non-existing element
            search_values.append(num_ops * 10) 
            
    # Helper function for search since your class lacks a dedicated search method.
    def search_list(list_obj, data):
        # This is an O(N) operation
        for item in list_obj:
            if item == data:
                return True
        return False
        
    start_time = time.time()
    found_count = 0
    for value in search_values:
        if search_list(list_to_test, value):
            found_count += 1
    end_time = time.time()

    print(f"   Total searches performed: {num_ops:,}")
    print(f"   Items found: {found_count:,}")
    print(f"   Time taken for {num_ops:,} searches: {end_time - start_time:.4f} seconds")

    
    # 3. STRESS DELETION (Head and Arbitrary Index Deletion)
    print("\n--- TEST 3: Deletion Stress (Mixed O(1) and O(N^2) Operations) ---")
    
    # Calculate the total number of items to delete
    elements_to_delete = len(list_to_test) // 2 
    
    start_time = time.time()
    
    # 50% O(1) deletions
    for _ in range(elements_to_delete // 2):
        if not list_to_test.is_empty():
            # Using delete_head() which is O(1) in your code
            list_to_test.delete_head() 

    # 50% O(N) deletions (via arbitrary index)
    # The actual complexity is O(N^2) over all deletions due to the repeated call to len()
    for _ in range(elements_to_delete - (elements_to_delete // 2)):
        if not list_to_test.is_empty():
            # Must call len() inside the loop to get the current size (The O(N) part)
            list_len = len(list_to_test) 
            if list_len > 0:
                random_index = random.randint(0, list_len - 1)
                list_to_test.delete_at_nth(random_index)
            
    end_time = time.time()
    
    print(f"   Total deletions performed: {elements_to_delete:,}")
    print(f"   Remaining elements: {len(list_to_test):,}")
    print(f"   Time taken for {elements_to_delete:,} deletions: {end_time - start_time:.4f} seconds")
    print("======================================================")


if __name__ == "__main__":
    run_stress_test(NUM_OPERATIONS)