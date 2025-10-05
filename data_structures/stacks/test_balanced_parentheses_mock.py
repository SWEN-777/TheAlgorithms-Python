import unittest
from unittest.mock import Mock, patch, MagicMock, call
from data_structures.stacks.balanced_parentheses import balanced_parentheses
from data_structures.stacks.stack import Stack


class TestBalancedParenthesesMock(unittest.TestCase):

    @patch('data_structures.stacks.balanced_parentheses.Stack')
    def test_stack_push_called_for_opening_bracket(self, mock_stack_class):
        mock_stack = MagicMock()
        mock_stack.is_empty.return_value = True
        mock_stack_class.return_value = mock_stack

        balanced_parentheses("(")

        mock_stack.push.assert_called()

    @patch('data_structures.stacks.balanced_parentheses.Stack')
    def test_stack_pop_called_for_closing_bracket(self, mock_stack_class):
        mock_stack = MagicMock()
        mock_stack.is_empty.side_effect = [False, True]
        mock_stack.pop.return_value = '('
        mock_stack_class.return_value = mock_stack

        balanced_parentheses("()")

        mock_stack.pop.assert_called()

    @patch('data_structures.stacks.balanced_parentheses.Stack')
    def test_multiple_push_operations(self, mock_stack_class):
        mock_stack = MagicMock()
        mock_stack.is_empty.side_effect = [False, False, False, True]
        mock_stack.pop.side_effect = ['{', '[', '(']
        mock_stack_class.return_value = mock_stack

        balanced_parentheses("abc")

        self.assertEqual(mock_stack.push.call_count, 3)

    @patch('data_structures.stacks.balanced_parentheses.Stack')
    def test_stack_empty_check_for_balanced(self, mock_stack_class):
        mock_stack = MagicMock()
        mock_stack.is_empty.side_effect = [False, True]
        mock_stack.pop.return_value = '('
        mock_stack_class.return_value = mock_stack

        result = balanced_parentheses("()")

        self.assertTrue(result)

    @patch('data_structures.stacks.balanced_parentheses.Stack')
    def test_stack_not_empty_returns_false(self, mock_stack_class):
        mock_stack = MagicMock()
        mock_stack.is_empty.return_value = False
        mock_stack_class.return_value = mock_stack

        result = balanced_parentheses("((")

        self.assertFalse(result)

    def test_empty_string_returns_true(self):
        result = balanced_parentheses("")

        self.assertTrue(result)

    def test_only_opening_brackets_returns_false(self):
        result = balanced_parentheses("(((")

        self.assertFalse(result)

    def test_only_closing_brackets_returns_false(self):
        result = balanced_parentheses(")))")

        self.assertFalse(result)

    def test_mismatched_brackets_returns_false(self):
        result = balanced_parentheses("(]")

        self.assertFalse(result)

    def test_nested_balanced_brackets(self):
        result = balanced_parentheses("([{}])")

        self.assertTrue(result)

    def test_string_with_non_bracket_characters(self):
        result = balanced_parentheses("a(b)c")

        self.assertTrue(result)

    def test_complex_expression_balanced(self):
        result = balanced_parentheses("if(condition){code[here]()}")

        self.assertTrue(result)

    def test_complex_expression_unbalanced(self):
        result = balanced_parentheses("if(condition{code[here]()}")

        self.assertFalse(result)

    @patch('data_structures.stacks.balanced_parentheses.Stack')
    def test_bracket_pairs_dict_usage(self, mock_stack_class):
        mock_stack = MagicMock()
        mock_stack.is_empty.side_effect = [False, True]
        mock_stack.pop.return_value = '('
        mock_stack_class.return_value = mock_stack

        result = balanced_parentheses("()")

        self.assertTrue(result)

    def test_mixed_brackets_and_text(self):
        result = balanced_parentheses("function(param1, param2[index])")

        self.assertTrue(result)

    def test_single_opening_bracket(self):
        result = balanced_parentheses("(")

        self.assertFalse(result)

    def test_single_closing_bracket(self):
        result = balanced_parentheses(")")

        self.assertFalse(result)

    def test_alternating_brackets(self):
        result = balanced_parentheses("()()()")

        self.assertTrue(result)

    def test_deeply_nested_brackets(self):
        result = balanced_parentheses("(((())))")

        self.assertTrue(result)

    @patch('data_structures.stacks.balanced_parentheses.Stack')
    def test_pop_returns_wrong_bracket(self, mock_stack_class):
        mock_stack = MagicMock()
        mock_stack.is_empty.return_value = False
        mock_stack.pop.return_value = '['
        mock_stack_class.return_value = mock_stack

        result = balanced_parentheses("(}")

        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
