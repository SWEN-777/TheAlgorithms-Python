import unittest

from data_structures.suffix_tree.suffix_tree import SuffixTree


class TestSuffixTreeEdgeCases(unittest.TestCase):


    def test_single_character_and_empty_string_handling(self) -> None:


        single_char_tree = SuffixTree("a")
        assert single_char_tree.search("a")
        assert single_char_tree.search("")  # Empty pattern should always be found
        assert not single_char_tree.search("b")
        assert not single_char_tree.search("aa")


        empty_tree = SuffixTree("")
        assert empty_tree.search("")
        assert not empty_tree.search("a")


        assert single_char_tree.text == "a"
        assert single_char_tree.root is not None
        assert len(single_char_tree.root.children) == 1
        assert "a" in single_char_tree.root.children


        assert empty_tree.text == ""
        assert empty_tree.root is not None
        assert len(empty_tree.root.children) == 0

    def test_repeating_patterns_and_overlapping_suffixes(self) -> None:


        repetitive_tree = SuffixTree("aaaa")


        expected_patterns = ["a", "aa", "aaa", "aaaa"]
        for pattern in expected_patterns:
            assert repetitive_tree.search(pattern), f"'{pattern}' should be found"


        assert not repetitive_tree.search("aaaaa")
        assert not repetitive_tree.search("b")
        assert not repetitive_tree.search("ab")


        alternating_tree = SuffixTree("abab")


        overlapping_patterns = [
            ("a", True), ("b", True), ("ab", True), ("ba", True),
            ("aba", True), ("bab", True), ("abab", True),
            ("aa", False), ("bb", False), ("abc", False)
        ]

        for pattern, expected in overlapping_patterns:
            result = alternating_tree.search(pattern)
            assert result == expected, f"'{pattern}' in 'abab': got {result}"


        assert len(repetitive_tree.root.children) == 1
        assert "a" in repetitive_tree.root.children


        node = repetitive_tree.root
        for _i in range(4):
            assert "a" in node.children
            node = node.children["a"]


if __name__ == "__main__":
    unittest.main()
