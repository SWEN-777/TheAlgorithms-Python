import unittest
from io import StringIO
from unittest.mock import patch

from data_structures.trie.radix_tree import RadixNode


class TestRadixTreeMock(unittest.TestCase):

    def test_match_returns_correct_tuple(self):
        node = RadixNode("myprefix")

        common, remaining_prefix, remaining_word = node.match("mystring")

        assert common == "my"
        assert remaining_prefix == "prefix"
        assert remaining_word == "string"

    def test_match_complete_match(self):
        node = RadixNode("test")

        common, remaining_prefix, remaining_word = node.match("test")

        assert common == "test"
        assert remaining_prefix == ""
        assert remaining_word == ""

    def test_match_no_common_substring(self):
        node = RadixNode("abc")

        common, remaining_prefix, remaining_word = node.match("xyz")

        assert common == ""
        assert remaining_prefix == "abc"
        assert remaining_word == "xyz"

    def test_insert_word_as_prefix(self):
        root = RadixNode()

        root.insert("myprefix")

        assert "m" in root.nodes
        assert root.nodes["m"].is_leaf

    def test_insert_many_words(self):
        root = RadixNode()
        words = ["test", "testing", "tester"]

        root.insert_many(words)

        assert root.find("test")
        assert root.find("testing")
        assert root.find("tester")

    def test_find_existing_word(self):
        root = RadixNode()
        root.insert("hello")

        result = root.find("hello")

        assert result

    def test_find_non_existing_word(self):
        root = RadixNode()
        root.insert("hello")

        result = root.find("world")

        assert not result

    def test_find_prefix_of_word(self):
        root = RadixNode()
        root.insert("testing")

        result = root.find("test")

        assert not result

    def test_delete_existing_word(self):
        root = RadixNode()
        root.insert("test")

        result = root.delete("test")

        assert result
        assert not root.find("test")

    def test_delete_non_existing_word(self):
        root = RadixNode()
        root.insert("test")

        result = root.delete("hello")

        assert not result

    def test_delete_with_remaining_children(self):
        root = RadixNode()
        root.insert("test")
        root.insert("testing")

        root.delete("test")

        assert not root.find("test")
        assert root.find("testing")

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_tree_outputs_text(self, mock_stdout):
        root = RadixNode()
        root.insert("test")

        root.print_tree()

        output = mock_stdout.getvalue()
        assert "test" in output

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_tree_leaf_indicator(self, mock_stdout):
        root = RadixNode()
        root.insert("word")

        root.print_tree()

        output = mock_stdout.getvalue()
        assert "(leaf)" in output

    def test_insert_empty_string(self):
        root = RadixNode()

        root.insert("")

        assert root.is_leaf

    def test_node_prefix_attribute(self):
        node = RadixNode("testprefix")

        assert node.prefix == "testprefix"

    def test_node_is_leaf_default_false(self):
        node = RadixNode("test")

        assert not node.is_leaf

    def test_node_is_leaf_set_true(self):
        node = RadixNode("test", is_leaf=True)

        assert node.is_leaf

    def test_insert_creates_intermediate_nodes(self):
        root = RadixNode()

        root.insert("testing")

        assert "t" in root.nodes

    def test_multiple_inserts_with_common_prefix(self):
        root = RadixNode()

        root.insert("test")
        root.insert("testing")
        root.insert("tester")

        assert root.find("test")
        assert root.find("testing")
        assert root.find("tester")

    def test_delete_merges_nodes(self):
        root = RadixNode()
        root.insert("test")
        root.insert("testing")

        root.delete("testing")

        assert root.find("test")
        assert not root.find("testing")

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_tree_empty_root(self, mock_stdout):
        root = RadixNode()

        root.print_tree()

        output = mock_stdout.getvalue()
        assert output.strip() == ""

    def test_find_partial_match(self):
        root = RadixNode()
        root.insert("banana")

        result = root.find("ban")

        assert not result

    def test_insert_duplicate_word(self):
        root = RadixNode()
        root.insert("word")
        root.insert("word")

        assert root.find("word")

    def test_case_sensitive_operations(self):
        root = RadixNode()
        root.insert("Test")

        assert root.find("Test")
        assert not root.find("test")

    def test_special_characters_in_words(self):
        root = RadixNode()
        root.insert("test@123")

        assert root.find("test@123")


if __name__ == "__main__":
    unittest.main()
