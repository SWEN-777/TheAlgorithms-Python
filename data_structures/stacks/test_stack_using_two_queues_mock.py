import unittest
from unittest.mock import Mock, patch, MagicMock
from collections import deque
from data_structures.stacks.stack_using_two_queues import StackWithQueues


class TestStackWithQueuesMock(unittest.TestCase):

    def test_push_with_mocked_deque(self):
        stack = StackWithQueues()
        stack.main_queue = MagicMock(spec=deque)
        stack.temp_queue = MagicMock(spec=deque)

        stack.main_queue.__len__.return_value = 0
        stack.main_queue.__bool__.return_value = False

        stack.push(10)

        stack.temp_queue.append.assert_called_with(10)

    @patch('data_structures.stacks.stack_using_two_queues.deque')
    def test_push_transfers_elements_correctly(self, mock_deque_class):
        stack = StackWithQueues()
        stack.main_queue = deque([1, 2, 3])
        stack.temp_queue = deque()

        stack.push(4)

        self.assertEqual(stack.main_queue[0], 4)

    def test_pop_from_empty_raises_error(self):
        stack = StackWithQueues()

        with self.assertRaises(IndexError):
            stack.pop()

    def test_peek_on_empty_returns_none(self):
        stack = StackWithQueues()

        result = stack.peek()

        self.assertIsNone(result)

    def test_peek_returns_top_element(self):
        stack = StackWithQueues()
        stack.push(1)
        stack.push(2)

        result = stack.peek()

        self.assertEqual(result, 2)

    def test_multiple_push_pop_operations(self):
        stack = StackWithQueues()

        stack.push(1)
        stack.push(2)
        stack.push(3)

        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)

    @patch('builtins.input')
    @patch('builtins.print')
    def test_interactive_menu_push(self, mock_print, mock_input):
        mock_input.side_effect = ['1', '5', '4']

        stack = StackWithQueues()

        with patch('data_structures.stacks.stack_using_two_queues.StackWithQueues', return_value=stack):
            choice = mock_input()
            if choice == '1':
                element = int(mock_input())
                stack.push(element)

        self.assertEqual(stack.peek(), 5)

    @patch('builtins.input')
    @patch('builtins.print')
    def test_interactive_menu_pop(self, mock_print, mock_input):
        stack = StackWithQueues()
        stack.push(10)

        mock_input.return_value = '2'

        choice = mock_input()
        if choice == '2':
            result = stack.pop()

        self.assertEqual(result, 10)

    @patch('builtins.input')
    @patch('builtins.print')
    def test_interactive_menu_peek(self, mock_print, mock_input):
        stack = StackWithQueues()
        stack.push(20)

        mock_input.return_value = '3'

        choice = mock_input()
        if choice == '3':
            result = stack.peek()

        self.assertEqual(result, 20)

    def test_stack_operations_sequence(self):
        stack = StackWithQueues()

        stack.push(10)
        self.assertEqual(stack.peek(), 10)

        stack.push(20)
        self.assertEqual(stack.peek(), 20)

        stack.push(30)
        self.assertEqual(stack.pop(), 30)
        self.assertEqual(stack.peek(), 20)


if __name__ == "__main__":
    unittest.main()
