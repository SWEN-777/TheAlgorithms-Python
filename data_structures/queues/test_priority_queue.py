import unittest
from priority_queue_using_list import (
    FixedPriorityQueue,
    ElementPriorityQueue,
    OverFlowError,
    UnderFlowError,
)


class TestFixedPriorityQueue(unittest.TestCase):
    """
    System tests for the FixedPriorityQueue class, which uses 3 internal lists.
    Focuses on priority order, FIFO, and exception handling.
    """

    def setUp(self):
        """Setup a fresh queue before each test."""
        self.fpq = FixedPriorityQueue()

    def test_01_priority_and_fifo_order(self):
        """Test the core functionality: highest priority (0) first, and FIFO for ties."""
        # Enqueue: (Priority, Data)
        self.fpq.enqueue(1, 70)  # P1
        self.fpq.enqueue(0, 10)  # P0 (Should be 1st)
        self.fpq.enqueue(2, 1)   # P2
        self.fpq.enqueue(0, 100) # P0 (Should be 2nd, FIFO with 10)
        self.fpq.enqueue(1, 7)   # P1 (Should be 4th, FIFO with 70)
        self.fpq.enqueue(2, 5)   # P2 (Should be 6th, FIFO with 1)

        # Expected Dequeue Order: P0 (FIFO), then P1 (FIFO), then P2 (FIFO)
        self.assertEqual(self.fpq.dequeue(), 10, "P0 (FIFO 1) failed")
        self.assertEqual(self.fpq.dequeue(), 100, "P0 (FIFO 2) failed")
        self.assertEqual(self.fpq.dequeue(), 70, "P1 (FIFO 1) failed")
        self.assertEqual(self.fpq.dequeue(), 7, "P1 (FIFO 2) failed")
        self.assertEqual(self.fpq.dequeue(), 1, "P2 (FIFO 1) failed")
        self.assertEqual(self.fpq.dequeue(), 5, "P2 (FIFO 2) failed")

        # Check if empty afterwards
        with self.assertRaises(UnderFlowError):
            self.fpq.dequeue()

    def test_02_underflow_exception(self):
        """Test dequeue on an empty queue."""
        with self.assertRaisesRegex(UnderFlowError, "All queues are empty"):
            self.fpq.dequeue()

    def test_03_string_representation(self):
        """Test the __str__ method output format."""
        self.fpq.enqueue(0, 10)
        self.fpq.enqueue(2, 1)
        self.assertEqual(str(self.fpq), "Priority 0: [10]\nPriority 1: []\nPriority 2: [1]")


class TestElementPriorityQueue(unittest.TestCase):
    """
    System tests for the ElementPriorityQueue class, where the element value is the priority.
    Focuses on min-value priority, internal list management, and exception handling.
    """

    def setUp(self):
        """Setup a fresh queue before each test."""
        self.epq = ElementPriorityQueue()

    def test_04_min_value_priority_order(self):
        """Test the core functionality: lowest element value is highest priority."""
        # Enqueue in a mixed order
        self.epq.enqueue(10)
        self.epq.enqueue(70)
        self.epq.enqueue(4)
        self.epq.enqueue(1)
        self.epq.enqueue(5)
        self.epq.enqueue(128)
        self.epq.enqueue(7)

        # Expected Dequeue Order: Lowest value first
        self.assertEqual(self.epq.dequeue(), 1)
        self.assertEqual(self.epq.dequeue(), 4)
        self.assertEqual(self.epq.dequeue(), 5)
        self.assertEqual(self.epq.dequeue(), 7)
        self.assertEqual(self.epq.dequeue(), 10)
        self.assertEqual(self.epq.dequeue(), 70)
        self.assertEqual(self.epq.dequeue(), 128)

        # Check if empty afterwards
        with self.assertRaises(UnderFlowError):
            self.epq.dequeue()

    def test_05_underflow_exception(self):
        """Test dequeue on an empty queue."""
        with self.assertRaisesRegex(UnderFlowError, "The queue is empty"):
            self.epq.dequeue()

    def test_06_overflow_exception(self):
        """Test enqueueing beyond the max capacity of 100."""
        # Fill the queue
        for i in range(100):
            self.epq.enqueue(i)

        # Attempt to add one more
        with self.assertRaisesRegex(OverFlowError, "Maximum queue size is 100"):
            self.epq.enqueue(101)

    def test_07_duplicate_elements(self):
        """Test that duplicate elements are handled correctly (min() and remove() logic)."""
        self.epq.enqueue(5)
        self.epq.enqueue(1)
        self.epq.enqueue(5) # Duplicate
        self.epq.enqueue(10)
        self.epq.enqueue(1) # Duplicate

        # Dequeue order: 1 (first), 1 (second), 5 (first), 5 (second), 10
        self.assertEqual(self.epq.dequeue(), 1)
        self.assertEqual(self.epq.dequeue(), 1)
        self.assertEqual(self.epq.dequeue(), 5)
        self.assertEqual(self.epq.dequeue(), 5)
        self.assertEqual(self.epq.dequeue(), 10)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
    