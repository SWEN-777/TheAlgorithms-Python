import unittest
from data_structures.stacks.balanced_parentheses import balanced_parentheses


class TestBalancedParenthesesEdgeCases(unittest.TestCase):
    

    def test_nested_mixed_brackets_with_characters(self) -> None:
       
        test_cases = [
            ("a{b[c(d)e]f}g", True),
            ("function(param1, param2[index])", True),
            ("array[index]{key: value(nested)}", True),
            ("if(condition){code[here]()}", True),
            ("text{[}]", False),  # Mixed up closing brackets
            ("code(with[mixed}brackets)", False),  # Wrong bracket order
        ]

        for expression, expected in test_cases:
            with self.subTest(expression=expression):
                result = balanced_parentheses(expression)
                self.assertEqual(
                    result,
                    expected,
                    f"Expression '{expression}' should return {expected}, got {result}"
                )

    def test_unbalanced_edge_cases(self) -> None:
        
        test_cases = [
            (")", False),  
            ("]", False),  
            ("}", False),  
            ("())", False),  
            ("(()", False),  
            ("([)]", False),  
            ("{[}]", False),  
            ("((())", False),  
            ("))(", False),  
        ]

        for expression, expected in test_cases:
            with self.subTest(expression=expression):
                result = balanced_parentheses(expression)
                self.assertEqual(
                    result,
                    expected,
                    f"Expression '{expression}' should return {expected}, got {result}"
                )


if __name__ == "__main__":
    unittest.main()