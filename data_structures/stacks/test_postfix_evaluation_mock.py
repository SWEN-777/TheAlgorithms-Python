import unittest
from unittest.mock import patch, MagicMock
from data_structures.stacks.postfix_evaluation import evaluate, parse_token, OPERATORS


class TestPostfixEvaluationMock(unittest.TestCase):

    @patch('builtins.print')
    def test_evaluate_with_verbose_mode(self, mock_print):
        expression = ["2", "3", "+"]

        result = evaluate(expression, verbose=True)

        self.assertEqual(result, 5.0)
        self.assertTrue(mock_print.called)

    @patch('builtins.print')
    def test_verbose_output_called_multiple_times(self, mock_print):
        expression = ["5", "6", "9", "*", "+"]

        evaluate(expression, verbose=True)

        self.assertGreater(mock_print.call_count, 1)

    @patch('data_structures.stacks.postfix_evaluation.OPERATORS')
    def test_evaluate_with_mocked_operators(self, mock_operators):
        mock_operators.__getitem__ = MagicMock(side_effect=lambda x: {
            '+': lambda a, b: a + b,
            '*': lambda a, b: a * b
        }[x])
        mock_operators.__contains__ = MagicMock(side_effect=lambda x: x in ['+', '*'])

        expression = ["2", "3", "+"]

        result = evaluate(expression, verbose=False)

        self.assertEqual(result, 5.0)

    def test_parse_token_valid_number(self):
        result = parse_token("42")

        self.assertEqual(result, 42.0)
        self.assertIsInstance(result, float)

    def test_parse_token_valid_operator(self):
        result = parse_token("+")

        self.assertEqual(result, "+")

    def test_parse_token_invalid_raises_error(self):
        with self.assertRaises(ValueError) as context:
            parse_token("invalid")

        self.assertIn("neither a number nor a valid operator", str(context.exception))

    def test_evaluate_empty_expression(self):
        result = evaluate([])

        self.assertEqual(result, 0)

    def test_evaluate_single_number(self):
        result = evaluate(["5"])

        self.assertEqual(result, 5.0)

    def test_evaluate_negative_numbers(self):
        result = evaluate(["-4", "5", "*"])

        self.assertEqual(result, -20.0)

    def test_evaluate_unary_minus(self):
        result = evaluate(["-", "5"])

        self.assertEqual(result, -5.0)

    def test_evaluate_unary_plus(self):
        result = evaluate(["+", "5"])

        self.assertEqual(result, 5.0)

    def test_evaluate_complex_expression(self):
        result = evaluate(["15", "7", "1", "1", "+", "-", "/", "3", "*"])

        self.assertEqual(result, 9.0)

    def test_evaluate_invalid_expression_raises_error(self):
        with self.assertRaises(ArithmeticError) as context:
            evaluate(["4", "-", "6", "7", "/", "9", "8"])

        self.assertIn("not a valid postfix expression", str(context.exception))

    @patch('builtins.print')
    def test_verbose_prints_table_header(self, mock_print):
        expression = ["2", "3", "+"]

        evaluate(expression, verbose=True)

        calls = [str(call) for call in mock_print.call_args_list]
        header_found = any("Symbol" in str(call) and "Action" in str(call) for call in calls)

        self.assertTrue(header_found)

    @patch('builtins.print')
    def test_verbose_prints_push_operations(self, mock_print):
        expression = ["5", "3", "+"]

        evaluate(expression, verbose=True)

        calls = [str(call) for call in mock_print.call_args_list]
        push_found = any("push" in str(call) for call in calls)

        self.assertTrue(push_found)

    @patch('builtins.print')
    def test_verbose_prints_pop_operations(self, mock_print):
        expression = ["5", "3", "+"]

        evaluate(expression, verbose=True)

        calls = [str(call) for call in mock_print.call_args_list]
        pop_found = any("pop" in str(call) for call in calls)

        self.assertTrue(pop_found)

    @patch('builtins.input')
    @patch('builtins.print')
    def test_interactive_loop_single_evaluation(self, mock_print, mock_input):
        mock_input.side_effect = ["2 3 +", "n", "n"]

        from data_structures.stacks.postfix_evaluation import evaluate

        expression = mock_input().split(" ")
        verbose_choice = mock_input().strip().lower() == "y"
        result = evaluate(expression, verbose_choice)

        self.assertEqual(result, 5.0)

    def test_evaluate_division(self):
        result = evaluate(["10", "2", "/"])

        self.assertEqual(result, 5.0)

    def test_evaluate_power_operation(self):
        result = evaluate(["2", "3", "^"])

        self.assertEqual(result, 8.0)

    def test_evaluate_with_decimals(self):
        result = evaluate(["2.5", "2", "*"])

        self.assertEqual(result, 5.0)


if __name__ == "__main__":
    unittest.main()
