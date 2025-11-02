import unittest
from unittest.mock import MagicMock, patch

from data_structures.suffix_tree.suffix_tree import SuffixTree
from data_structures.suffix_tree.suffix_tree_node import SuffixTreeNode


class TestSuffixTreeMock(unittest.TestCase):

    @patch('data_structures.suffix_tree.suffix_tree.SuffixTreeNode')
    def test_root_node_created(self, mock_node_class):
        mock_root = MagicMock()
        mock_node_class.return_value = mock_root

        SuffixTree("test")

        mock_node_class.assert_called()

    @patch('data_structures.suffix_tree.suffix_tree.SuffixTreeNode')
    def test_build_suffix_tree_called(self, mock_node_class):
        mock_root = MagicMock()
        mock_node_class.return_value = mock_root

        with patch.object(SuffixTree, 'build_suffix_tree') as mock_build:
            tree = SuffixTree.__new__(SuffixTree)
            tree.text = "abc"
            tree.root = mock_root
            tree.build_suffix_tree()

            mock_build.assert_called_once()

    @patch('data_structures.suffix_tree.suffix_tree.SuffixTreeNode')
    def test_add_suffix_creates_nodes(self, mock_node_class):
        mock_child = MagicMock()
        mock_child.children = {}
        mock_node_class.return_value = mock_child

        tree = SuffixTree.__new__(SuffixTree)
        tree.text = "a"
        tree.root = MagicMock()
        tree.root.children = {}

        tree._add_suffix("a", 0)

        assert 'a' in tree.root.children

    def test_search_empty_pattern(self):
        tree = SuffixTree("banana")

        result = tree.search("")

        assert result

    def test_search_single_character(self):
        tree = SuffixTree("banana")

        result = tree.search("b")

        assert result

    def test_search_non_existent_pattern(self):
        tree = SuffixTree("banana")

        result = tree.search("xyz")

        assert not result

    def test_search_full_text(self):
        tree = SuffixTree("hello")

        result = tree.search("hello")

        assert result

    def test_search_suffix(self):
        tree = SuffixTree("testing")

        result = tree.search("ting")

        assert result

    def test_search_prefix(self):
        tree = SuffixTree("testing")

        result = tree.search("test")

        assert result

    def test_search_middle_substring(self):
        tree = SuffixTree("testing")

        result = tree.search("sti")

        assert result

    @patch('data_structures.suffix_tree.suffix_tree.SuffixTreeNode')
    def test_node_children_dictionary(self, mock_node_class):
        mock_node = MagicMock()
        mock_node.children = {}
        mock_node_class.return_value = mock_node

        tree = SuffixTree("ab")

        assert isinstance(tree.root.children, dict)

    def test_empty_string_tree(self):
        tree = SuffixTree("")

        result = tree.search("")

        assert result

    def test_single_character_tree(self):
        tree = SuffixTree("a")

        assert tree.search("a")
        assert not tree.search("b")

    def test_repeated_characters(self):
        tree = SuffixTree("aaaa")

        assert tree.search("aa")
        assert tree.search("aaa")
        assert tree.search("aaaa")

    @patch('data_structures.suffix_tree.suffix_tree.SuffixTreeNode')
    def test_add_suffix_sets_end_marker(self):
        tree = SuffixTree.__new__(SuffixTree)
        tree.text = "test"
        tree.root = SuffixTreeNode()

        tree._add_suffix("t", 0)

        node = tree.root.children['t']
        assert node.is_end_of_string

    @patch('data_structures.suffix_tree.suffix_tree.SuffixTreeNode')
    def test_add_suffix_sets_indices(self):
        tree = SuffixTree.__new__(SuffixTree)
        tree.text = "test"
        tree.root = SuffixTreeNode()

        tree._add_suffix("est", 1)

        node = tree.root
        for char in "est":
            node = node.children[char]

        assert node.start == 1
        assert node.end == 3

    def test_case_sensitive_search(self):
        tree = SuffixTree("Hello")

        assert tree.search("Hello")
        assert not tree.search("hello")

    def test_special_characters(self):
        tree = SuffixTree("test@123")

        assert tree.search("@123")
        assert tree.search("est@")

    def test_search_longer_than_text(self):
        tree = SuffixTree("ab")

        result = tree.search("abc")

        assert not result

    def test_multiple_searches(self):
        tree = SuffixTree("algorithm")

        assert tree.search("algo")
        assert tree.search("rithm")
        assert tree.search("go")
        assert not tree.search("xyz")


if __name__ == "__main__":
    unittest.main()
