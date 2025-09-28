import unittest
from data_structures.suffix_tree.suffix_tree import SuffixTree


class TestSuffixTreeEdgeCases(unittest.TestCase):
    

    def test_single_character_and_empty_string_handling(self) -> None:
       
        
        single_char_tree = SuffixTree("a")
        self.assertTrue(single_char_tree.search("a"))
        self.assertTrue(single_char_tree.search(""))  # Empty pattern should always be found
        self.assertFalse(single_char_tree.search("b"))
        self.assertFalse(single_char_tree.search("aa"))

        
        empty_tree = SuffixTree("")
        self.assertTrue(empty_tree.search(""))  
        self.assertFalse(empty_tree.search("a"))  

        
        self.assertEqual(single_char_tree.text, "a")
        self.assertIsNotNone(single_char_tree.root)
        self.assertEqual(len(single_char_tree.root.children), 1)
        self.assertIn("a", single_char_tree.root.children)

        
        self.assertEqual(empty_tree.text, "")
        self.assertIsNotNone(empty_tree.root)
        self.assertEqual(len(empty_tree.root.children), 0)

    def test_repeating_patterns_and_overlapping_suffixes(self) -> None:
      
       
        repetitive_tree = SuffixTree("aaaa")

        
        expected_patterns = ["a", "aa", "aaa", "aaaa"]
        for pattern in expected_patterns:
            self.assertTrue(
                repetitive_tree.search(pattern),
                f"Pattern '{pattern}' should be found in 'aaaa'"
            )

        
        self.assertFalse(repetitive_tree.search("aaaaa"))
        self.assertFalse(repetitive_tree.search("b"))
        self.assertFalse(repetitive_tree.search("ab"))

        
        alternating_tree = SuffixTree("abab")

        
        overlapping_patterns = [
            ("a", True), ("b", True), ("ab", True), ("ba", True),
            ("aba", True), ("bab", True), ("abab", True),
            ("aa", False), ("bb", False), ("abc", False)
        ]

        for pattern, expected in overlapping_patterns:
            result = alternating_tree.search(pattern)
            self.assertEqual(
                result, expected,
                f"Pattern '{pattern}' in 'abab': expected {expected}, got {result}"
            )

        
        self.assertEqual(len(repetitive_tree.root.children), 1)
        self.assertIn("a", repetitive_tree.root.children)

        
        node = repetitive_tree.root
        for i in range(4):  
            self.assertIn("a", node.children)
            node = node.children["a"]


if __name__ == "__main__":
    unittest.main()