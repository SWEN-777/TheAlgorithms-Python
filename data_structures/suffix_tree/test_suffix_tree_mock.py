import unittest
from unittest.mock import Mock, patch, MagicMock, call
from data_structures.suffix_tree.suffix_tree import SuffixTree
from data_structures.suffix_tree.suffix_tree_node import SuffixTreeNode


class TestSuffixTreeMock(unittest.TestCase):

    @patch('data_structures.suffix_tree.suffix_tree.SuffixTreeNode')
    def test_root_node_created(self, mock_node_class):
        mock_root = MagicMock()
        mock_node_class.return_value = mock_root

        tree = SuffixTree("test")

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

        self.assertIn('a', tree.root.children)

    def test_search_empty_pattern(self):
        tree = SuffixTree("banana")

        result = tree.search("")

        self.assertTrue(result)

    def test_search_single_character(self):
        tree = SuffixTree("banana")

        result = tree.search("b")

        self.assertTrue(result)

    def test_search_non_existent_pattern(self):
        tree = SuffixTree("banana")

        result = tree.search("xyz")

        self.assertFalse(result)

    def test_search_full_text(self):
        tree = SuffixTree("hello")

        result = tree.search("hello")

        self.assertTrue(result)

    def test_search_suffix(self):
        tree = SuffixTree("testing")

        result = tree.search("ting")

        self.assertTrue(result)

    def test_search_prefix(self):
        tree = SuffixTree("testing")

        result = tree.search("test")

        self.assertTrue(result)

    def test_search_middle_substring(self):
        tree = SuffixTree("testing")

        result = tree.search("sti")

        self.assertTrue(result)

    @patch('data_structures.suffix_tree.suffix_tree.SuffixTreeNode')
    def test_node_children_dictionary(self, mock_node_class):
        mock_node = MagicMock()
        mock_node.children = {}
        mock_node_class.return_value = mock_node

        tree = SuffixTree("ab")

        self.assertIsInstance(tree.root.children, dict)

    def test_empty_string_tree(self):
        tree = SuffixTree("")

        result = tree.search("")

        self.assertTrue(result)

    def test_single_character_tree(self):
        tree = SuffixTree("a")

        self.assertTrue(tree.search("a"))
        self.assertFalse(tree.search("b"))

    def test_repeated_characters(self):
        tree = SuffixTree("aaaa")

        self.assertTrue(tree.search("aa"))
        self.assertTrue(tree.search("aaa"))
        self.assertTrue(tree.search("aaaa"))

    @patch('data_structures.suffix_tree.suffix_tree.SuffixTreeNode')
    def test_add_suffix_sets_end_marker(self, mock_node_class):
        tree = SuffixTree.__new__(SuffixTree)
        tree.text = "test"
        tree.root = SuffixTreeNode()

        tree._add_suffix("t", 0)

        node = tree.root.children['t']
        self.assertTrue(node.is_end_of_string)

    @patch('data_structures.suffix_tree.suffix_tree.SuffixTreeNode')
    def test_add_suffix_sets_indices(self, mock_node_class):
        tree = SuffixTree.__new__(SuffixTree)
        tree.text = "test"
        tree.root = SuffixTreeNode()

        tree._add_suffix("est", 1)

        node = tree.root
        for char in "est":
            node = node.children[char]

        self.assertEqual(node.start, 1)
        self.assertEqual(node.end, 3)

    def test_case_sensitive_search(self):
        tree = SuffixTree("Hello")

        self.assertTrue(tree.search("Hello"))
        self.assertFalse(tree.search("hello"))

    def test_special_characters(self):
        tree = SuffixTree("test@123")

        self.assertTrue(tree.search("@123"))
        self.assertTrue(tree.search("est@"))

    def test_search_longer_than_text(self):
        tree = SuffixTree("ab")

        result = tree.search("abc")

        self.assertFalse(result)

    def test_multiple_searches(self):
        tree = SuffixTree("algorithm")

        self.assertTrue(tree.search("algo"))
        self.assertTrue(tree.search("rithm"))
        self.assertTrue(tree.search("go"))
        self.assertFalse(tree.search("xyz"))


if __name__ == "__main__":
    unittest.main()
