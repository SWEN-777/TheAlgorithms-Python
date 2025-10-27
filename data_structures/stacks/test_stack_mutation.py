import unittest
from unittest.mock import Mock, patch, MagicMock
from collections import deque
from data_structures.stacks.stack_using_two_queues import StackWithQueues


class TestStackMutation(unittest.TestCase):

    def test_push_return_value_is_none(self):
        """Kills mutation from None to False in push() return annotation"""
        stack = StackWithQueues()
        result = stack.push(10)
        self.assertIsNone(result)
        self.assertIsNot(result, False)

    def test_peek_return_type_with_value(self):
        """Kills mutation from int | None to int & None in peek() return"""
        stack = StackWithQueues()
        stack.push(42)
        result = stack.peek()
        self.assertEqual(result, 42)
        self.assertIsInstance(result, int)
        self.assertIsNot(result, None)

    def test_peek_return_type_without_value(self):
        """Kills mutation from None to True in peek() return annotation"""
        stack = StackWithQueues()
        result = stack.peek()
        self.assertIsNone(result)
        self.assertIsNot(result, True)
        self.assertIsNot(result, False)

    def test_peek_returns_none_not_true(self):
        """Additional test to kill None -> True mutation in peek"""
        stack = StackWithQueues()
        self.assertIs(stack.peek(), None)
        self.assertIsNot(stack.peek(), True)

    def test_push_multiple_items_verify_order(self):
        """Test push operation maintains stack order"""
        stack = StackWithQueues()
        for i in range(5):
            result = stack.push(i)
            self.assertIsNone(result)

        self.assertEqual(stack.peek(), 4)

    def test_empty_stack_operations(self):
        """Test operations on empty stack"""
        stack = StackWithQueues()
        peek_result = stack.peek()

        self.assertIsNone(peek_result)
        self.assertFalse(peek_result is True)
        self.assertFalse(peek_result is False)

    def test_push_peek_sequence_verifies_none(self):
        """Comprehensive test for None vs True/False"""
        stack = StackWithQueues()

        self.assertIsNone(stack.peek())

        push_result = stack.push(100)
        self.assertIsNone(push_result)
        self.assertNotEqual(push_result, False)

        peek_result = stack.peek()
        self.assertEqual(peek_result, 100)
        self.assertIsNot(peek_result, None)

    def test_pop_then_peek_empty(self):
        """Test peek after popping all elements"""
        stack = StackWithQueues()
        stack.push(1)
        stack.pop()

        result = stack.peek()
        self.assertIsNone(result)
        self.assertIsNot(result, True)

    def test_push_returns_exactly_none(self):
        """Strict test that push returns None, not False"""
        stack = StackWithQueues()
        result = stack.push(5)

        self.assertTrue(result is None)
        self.assertFalse(result is False)
        self.assertFalse(result is True)

    def test_dataclass_fields_initialization(self):
        """Test that stack initializes correctly"""
        stack = StackWithQueues()

        self.assertIsInstance(stack.main_queue, deque)
        self.assertIsInstance(stack.temp_queue, deque)
        self.assertEqual(len(stack.main_queue), 0)
        self.assertEqual(len(stack.temp_queue), 0)

    def test_push_internal_state(self):
        """Test internal state after push"""
        stack = StackWithQueues()
        stack.push(10)

        self.assertEqual(len(stack.main_queue), 1)
        self.assertEqual(len(stack.temp_queue), 0)
        self.assertEqual(stack.main_queue[0], 10)

    def test_multiple_operations_sequence(self):
        """Test sequence of operations with return value checks"""
        stack = StackWithQueues()

        r1 = stack.push(1)
        self.assertIsNone(r1)

        r2 = stack.push(2)
        self.assertIsNone(r2)

        peek1 = stack.peek()
        self.assertEqual(peek1, 2)
        self.assertIsInstance(peek1, int)

        pop1 = stack.pop()
        self.assertEqual(pop1, 2)

        peek2 = stack.peek()
        self.assertEqual(peek2, 1)

        pop2 = stack.pop()
        self.assertEqual(pop2, 1)

        peek3 = stack.peek()
        self.assertIsNone(peek3)


if __name__ == "__main__":
    unittest.main()
