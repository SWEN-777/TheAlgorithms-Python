import unittest
# Assuming 'heap.py' is in the same directory and contains the Heap class
from heap import Heap 

class TestHeapMutations(unittest.TestCase):
    def setUp(self):
        # A consistent dataset that requires multiple heapify steps and comparisons
        self.data = [103, 9, 1, 7, 11, 15, 25, 201, 209, 107, 5]
        self.h = Heap()
        self.h.build_max_heap(self.data)
        # Expected heap state after build_max_heap
        self.expected_heap = [209, 201, 25, 103, 107, 15, 1, 9, 7, 11, 5]
        self.assertEqual(self.h.h, self.expected_heap)
        self.assertEqual(self.h.heap_size, 11)

    # ----------------------------------------
    # Index Calculation Tests
    # ----------------------------------------
    
    def test_parent_index_mutations(self):
        """KILLS MUTANTS IN parent_index"""
        # 1. Kills: `child_idx > 0` changed to `child_idx >= 0` (boundary check mutation)
        self.assertIsNone(self.h.parent_index(0), "Index 0 should have no parent (None)")
        # 2. Kills: `(child_idx - 1) // 2` changed (e.g., operator swap or wrong integer division)
        self.assertEqual(self.h.parent_index(3), 1, "Child 3's parent should be 1")
        self.assertEqual(self.h.parent_index(4), 1, "Child 4's parent should be 1")

    def test_child_index_boundary_mutations(self):
        """KILLS MUTANTS IN left_child_idx and right_child_idx"""
        # 1. Kills: `< self.heap_size` boundary check changed (e.g., to `<=`)
        # Index 5 has children 11 and 12, which are out of bounds (size is 11, max index is 10)
        self.assertIsNone(self.h.left_child_idx(5), "Left child of 5 should not exist (index 11)")
        self.assertIsNone(self.h.right_child_idx(5), "Right child of 5 should not exist (index 12)")
        
        # 2. Verifies correct index calculation (e.g., catches `2 * parent_idx + 1` mutation)
        self.assertEqual(self.h.left_child_idx(4), 9, "Left child of 4 is 9")

    # ----------------------------------------
    # Max Heapify Tests
    # ----------------------------------------

    def test_max_heapify_single_swap(self):
        """KILLS MUTANTS FOR RECURSION AND SWAP LOGIC IN max_heapify"""
        # Introduce a deep violation at index 1 (201 -> 1). This forces the '1' to sink two levels.
        # This test is crucial for ensuring the recursive call `self.max_heapify(violation)` is present.
        self.h.h[1] = 1
        self.h.max_heapify(1)
        
        # 1. Kills: Comparison operators (`>` changed to `>=`, `<`, or `!=`)
        self.assertEqual(self.h.h[1], 107, "Index 1 failed to promote the max value (107).")
        
        # 2. Kills: Missing recursive call (if recursion is missed, index 4 would be 1, not 11)
        # 3. Kills: Swap logic error (e.g., if only one swap is implemented, not two)
        self.assertEqual(self.h.h[4], 11, "The element 11 should have moved up to index 4 in the second swap.")
        self.assertEqual(self.h.h[9], 1, "The sinker (1) must reach its lowest resting place (index 9).")

    def test_max_heapify_multi_level_recursion_mutations(self):
        """KILLS MUTANTS IN max_heapify RECURSION and VIOLATION CHECK"""
        # Set up a new violation at root 0 that forces a swap down, then a subsequent swap down.
        # Original element 1 sinks two levels (0 -> 1 -> 4).
        self.h.h = [1, 201, 25, 103, 107, 15, 1, 9, 7, 11, 5]
        self.h.heap_size = 11
        self.h.max_heapify(0)
        
        # 1. Kills: `violation != index` check changed (e.g., to `violation == index`).
        # 2. Kills: Missing assignment of `violation = left_child` or `right_child`.
        self.assertEqual(self.h.h[0], 201, "Highest element failed to move to root.")
        self.assertEqual(self.h.h[1], 107, "Second-level element failed to move up (recursion failure).")

    def test_max_heapify_comparison_mutations(self):
        """KILLS MUTANTS FOR CHILD SELECTION LOGIC in max_heapify"""
        # Set up a case where the right child is the maximum (30 > 20).
        self.h.h = [10, 20, 30]
        self.h.heap_size = 3
        self.h.max_heapify(0)
        
        # 1. Kills: Comparison operators changed from `>` to `<` in child selection.
        # 2. Kills: Logic that fails to find the maximum of the two children (e.g., if it only checks the left child).
        self.assertEqual(self.h.h[0], 30, "max_heapify must select the *largest* of the two children.")

    # ----------------------------------------
    # Build Max Heap Tests
    # ----------------------------------------

    def test_build_max_heap_loop_range_mutations(self):
        """KILLS MUTANTS FOR LOOP RANGE IN build_max_heap"""
        # Test case where the starting point of the loop (heap_size // 2 - 1) is crucial.
        # For [1, 2, 3, 4, 5, 6, 7], size=7. Start index: 2.
        self.h.build_max_heap([1, 2, 3, 4, 5, 6, 7])
        
        # 1. Kills: Loop range mutation (e.g., `range(size // 2, ...)` or wrong step `-1`)
        self.assertEqual(self.h.h, [7, 5, 6, 4, 2, 1, 3], "Build max heap failed due to incorrect loop range or logic.")

    # ----------------------------------------
    # Extract Max Tests
    # ----------------------------------------

    def test_extract_max_size_two_mutations(self):
        """KILLS MUTANTS FOR SWAP, SIZE DECREMENT, and HEAPIFY CALL in extract_max"""
        self.h.build_max_heap([5, 10]) # Initial: [10, 5]
        
        max_val = self.h.extract_max()
        # 1. Kills: Missing size decrement (mutant: `self.heap_size -= 1` deleted)
        self.assertEqual(self.h.heap_size, 1, "Extract max failed to decrease size.")
        # 2. Kills: Missing heapify call (mutant: `self.max_heapify(0)` deleted)
        self.assertEqual(self.h.h, [5], "Extract max failed to perform swap or heapify.")

        # 3. Kills: Incorrect handling of size 1 case
        max_val = self.h.extract_max()
        self.assertEqual(max_val, 5, "Extract max (size 1 case) returned incorrect value.")

    def test_extract_max_empty_heap_mutation(self):
        """KILLS MUTANTS FOR EMPTY HEAP CHECK in extract_max"""
        self.h.build_max_heap([])
        # 1. Kills: Logic that prevents raising the exception on an empty heap (e.g., `else` block deleted)
        with self.assertRaises(Exception, msg="Extract max on empty heap must raise an exception."):
            self.h.extract_max()

    # ----------------------------------------
    # Insert Tests
    # ----------------------------------------

    def test_insert_bubble_to_root_mutations(self):
        """KILLS MUTANTS FOR BUBBLE-UP LOOP AND HEAPIFY CALL in insert"""
        self.h.build_max_heap([1, 5, 7, 15, 25])
        self.h.extract_max() # [15, 7, 5, 1] (size 4)
        
        # Insert 100, which must bubble all the way to index 0.
        self.h.insert(100)
        
        # 1. Kills: `while idx >= 0` loop condition changed (e.g., to `> 0` or `<=` initial index)
        # 2. Kills: Missing size increment (mutant: `self.heap_size += 1` deleted)
        # 3. Kills: Incorrect parent index calculation for next iteration (mutant: `idx = (idx - 1) // 2` error)
        self.assertEqual(self.h.h[0], 100, "Insert failed to bubble up to the root.")
        self.assertEqual(self.h.heap_size, 5, "Insert failed to increase heap size.")

    def test_insert_no_bubble_mutations(self):
        """KILLS MUTANTS FOR UNNECESSARY HEAPIFY CALLS in insert"""
        self.h.build_max_heap([1, 5, 7, 15, 25]) # [25, 15, 5, 1, 7]
        
        # Insert 0, which should not bubble at all.
        self.h.insert(0)
        
        # 1. Kills: Overly aggressive heapify (If the `max_heapify` logic incorrectly bubbles up 0)
        self.assertEqual(self.h.h[5], 0, "Insert failed to place element correctly.")
        self.assertGreater(self.h.h[2], self.h.h[5], "Heap property violated after no-bubble insert.")


    # ----------------------------------------
    # Heap Sort Tests
    # ----------------------------------------

    def test_heap_sort_mutations(self):
        """KILLS MUTANTS FOR LOOP RANGE, SIZE RESET, and SWAP in heap_sort"""
        self.h.build_max_heap([5, 1, 4, 2, 8]) # Initial: [8, 5, 4, 2, 1]
        
        self.h.heap_sort()
        
        # 1. Kills: Loop range mutation (e.g., `range(size - 1, 0, -1)` changed to `size` or `1`)
        self.assertEqual(self.h.h, [1, 2, 4, 5, 8], "Heap sort failed to produce a fully sorted array.")
        
        # 2. Kills: Missing heap size reset (mutant: `self.heap_size = size` deleted)
        self.assertEqual(self.h.heap_size, 5, "Heap sort failed to reset heap_size.")

        # 3. Kills: Failure to handle duplicates (test data includes 8, 8, 1, 1)
        self.h.build_max_heap([5, 1, 4, 2, 8, 8, 1])
        self.h.heap_sort()
        self.assertEqual(self.h.h, [1, 1, 2, 4, 5, 8, 8], "Heap sort failed with duplicates.")
