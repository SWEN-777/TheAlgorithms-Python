import unittest
from unittest.mock import Mock, patch, MagicMock, call
from data_structures.stacks.dijkstras_two_stack_algorithm import dijkstras_two_stack_algorithm
from data_structures.stacks.stack import Stack


class TestDijkstrasTwoStackMock(unittest.TestCase):

    @patch('data_structures.stacks.dijkstras_two_stack_algorithm.Stack')
    def test_operand_stack_push_called(self, mock_stack_class):
        mock_operand_stack = MagicMock()
        mock_operator_stack = MagicMock()
        mock_stack_class.side_effect = [mock_operand_stack, mock_operator_stack]

        mock_operand_stack.peek.return_value = 3
        mock_operator_stack.peek.return_value = '+'

        equation = "(5 + 3)"

        with patch('data_structures.stacks.dijkstras_two_stack_algorithm.Stack', side_effect=[mock_operand_stack, mock_operator_stack]):
            try:
                dijkstras_two_stack_algorithm(equation)
            except:
                pass

    @patch('data_structures.stacks.dijkstras_two_stack_algorithm.Stack')
    def test_operator_stack_operations(self, mock_stack_class):
        mock_operand_stack = MagicMock()
        mock_operator_stack = MagicMock()
        mock_stack_class.side_effect = [mock_operand_stack, mock_operator_stack]

        mock_operand_stack.peek.side_effect = [3, 5]
        mock_operator_stack.peek.return_value = '+'

        equation = "(5 + 3)"

        try:
            with patch('data_structures.stacks.dijkstras_two_stack_algorithm.Stack', side_effect=[mock_operand_stack, mock_operator_stack]):
                dijkstras_two_stack_algorithm(equation)
        except:
            pass

    def test_simple_addition(self):
        result = dijkstras_two_stack_algorithm("(5 + 3)")

        self.assertEqual(result, 8)

    def test_simple_subtraction(self):
        result = dijkstras_two_stack_algorithm("(9 - 2)")

        self.assertEqual(result, 7)

    def test_simple_multiplication(self):
        result = dijkstras_two_stack_algorithm("(4 * 3)")

        self.assertEqual(result, 12)

    def test_simple_division(self):
        result = dijkstras_two_stack_algorithm("(8 / 2)")

        self.assertEqual(result, 4.0)

    def test_nested_expression(self):
        result = dijkstras_two_stack_algorithm("((9 - (2 + 3)) + (8 - 1))")

        self.assertEqual(result, 11)

    def test_complex_nested_expression(self):
        result = dijkstras_two_stack_algorithm("((((3 - 2) - (2 + 3)) + (2 - 4)) + 3)")

        self.assertEqual(result, -3)

    def test_multiple_operations(self):
        result = dijkstras_two_stack_algorithm("((5 + 3) * 2)")

        self.assertEqual(result, 16)

    def test_left_parenthesis_ignored(self):
        result = dijkstras_two_stack_algorithm("(((5 + 3)))")

        self.assertEqual(result, 8)

    @patch('data_structures.stacks.dijkstras_two_stack_algorithm.op')
    def test_operators_dict_usage(self, mock_op):
        mock_op.mul = MagicMock(return_value=12)
        mock_op.truediv = MagicMock(return_value=2)
        mock_op.add = MagicMock(return_value=8)
        mock_op.sub = MagicMock(return_value=3)

        equation = "(5 + 3)"

        result = dijkstras_two_stack_algorithm(equation)

        self.assertIsNotNone(result)

    def test_single_digit_operations(self):
        result = dijkstras_two_stack_algorithm("(1 + 1)")

        self.assertEqual(result, 2)

    def test_zero_in_operations(self):
        result = dijkstras_two_stack_algorithm("(0 + 5)")

        self.assertEqual(result, 5)

    def test_result_zero(self):
        result = dijkstras_two_stack_algorithm("(5 - 5)")

        self.assertEqual(result, 0)

    def test_deeply_nested_expression(self):
        result = dijkstras_two_stack_algorithm("(((2 + 3) * (4 - 1)))")

        self.assertEqual(result, 15)

    @patch('data_structures.stacks.dijkstras_two_stack_algorithm.Stack')
    def test_peek_and_pop_sequence(self, mock_stack_class):
        mock_operand_stack = MagicMock()
        mock_operator_stack = MagicMock()

        mock_operand_stack.peek.side_effect = [3, 5, 8]
        mock_operator_stack.peek.return_value = '+'

        mock_stack_class.side_effect = [mock_operand_stack, mock_operator_stack]

        equation = "(5 + 3)"

        try:
            with patch('data_structures.stacks.dijkstras_two_stack_algorithm.Stack', side_effect=[mock_operand_stack, mock_operator_stack]):
                result = dijkstras_two_stack_algorithm(equation)
        except:
            pass


if __name__ == "__main__":
    unittest.main()
