import unittest
from unittest.mock import Mock, patch, MagicMock, call
from io import StringIO
from data_structures.trie.radix_tree import RadixNode


class TestRadixTreeMock(unittest.TestCase):

    def test_match_returns_correct_tuple(self):
        node = RadixNode("myprefix")

        common, remaining_prefix, remaining_word = node.match("mystring")

        self.assertEqual(common, "my")
        self.assertEqual(remaining_prefix, "prefix")
        self.assertEqual(remaining_word, "string")

    def test_match_complete_match(self):
        node = RadixNode("test")

        common, remaining_prefix, remaining_word = node.match("test")

        self.assertEqual(common, "test")
        self.assertEqual(remaining_prefix, "")
        self.assertEqual(remaining_word, "")

    def test_match_no_common_substring(self):
        node = RadixNode("abc")

        common, remaining_prefix, remaining_word = node.match("xyz")

        self.assertEqual(common, "")
        self.assertEqual(remaining_prefix, "abc")
        self.assertEqual(remaining_word, "xyz")

    def test_insert_word_as_prefix(self):
        root = RadixNode()

        root.insert("myprefix")

        self.assertIn("m", root.nodes)
        self.assertTrue(root.nodes["m"].is_leaf)

    def test_insert_many_words(self):
        root = RadixNode()
        words = ["test", "testing", "tester"]

        root.insert_many(words)

        self.assertTrue(root.find("test"))
        self.assertTrue(root.find("testing"))
        self.assertTrue(root.find("tester"))

    def test_find_existing_word(self):
        root = RadixNode()
        root.insert("hello")

        result = root.find("hello")

        self.assertTrue(result)

    def test_find_non_existing_word(self):
        root = RadixNode()
        root.insert("hello")

        result = root.find("world")

        self.assertFalse(result)

    def test_find_prefix_of_word(self):
        root = RadixNode()
        root.insert("testing")

        result = root.find("test")

        self.assertFalse(result)

    def test_delete_existing_word(self):
        root = RadixNode()
        root.insert("test")

        result = root.delete("test")

        self.assertTrue(result)
        self.assertFalse(root.find("test"))

    def test_delete_non_existing_word(self):
        root = RadixNode()
        root.insert("test")

        result = root.delete("hello")

        self.assertFalse(result)

    def test_delete_with_remaining_children(self):
        root = RadixNode()
        root.insert("test")
        root.insert("testing")

        root.delete("test")

        self.assertFalse(root.find("test"))
        self.assertTrue(root.find("testing"))

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_tree_outputs_text(self, mock_stdout):
        root = RadixNode()
        root.insert("test")

        root.print_tree()

        output = mock_stdout.getvalue()
        self.assertIn("test", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_tree_leaf_indicator(self, mock_stdout):
        root = RadixNode()
        root.insert("word")

        root.print_tree()

        output = mock_stdout.getvalue()
        self.assertIn("(leaf)", output)

    def test_insert_empty_string(self):
        root = RadixNode()

        root.insert("")

        self.assertTrue(root.is_leaf)

    def test_node_prefix_attribute(self):
        node = RadixNode("testprefix")

        self.assertEqual(node.prefix, "testprefix")

    def test_node_is_leaf_default_false(self):
        node = RadixNode("test")

        self.assertFalse(node.is_leaf)

    def test_node_is_leaf_set_true(self):
        node = RadixNode("test", is_leaf=True)

        self.assertTrue(node.is_leaf)

    def test_insert_creates_intermediate_nodes(self):
        root = RadixNode()

        root.insert("testing")

        self.assertIn("t", root.nodes)

    def test_multiple_inserts_with_common_prefix(self):
        root = RadixNode()

        root.insert("test")
        root.insert("testing")
        root.insert("tester")

        self.assertTrue(root.find("test"))
        self.assertTrue(root.find("testing"))
        self.assertTrue(root.find("tester"))

    def test_delete_merges_nodes(self):
        root = RadixNode()
        root.insert("test")
        root.insert("testing")

        root.delete("testing")

        self.assertTrue(root.find("test"))
        self.assertFalse(root.find("testing"))

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_tree_empty_root(self, mock_stdout):
        root = RadixNode()

        root.print_tree()

        output = mock_stdout.getvalue()
        self.assertEqual(output.strip(), "")

    def test_find_partial_match(self):
        root = RadixNode()
        root.insert("banana")

        result = root.find("ban")

        self.assertFalse(result)

    def test_insert_duplicate_word(self):
        root = RadixNode()
        root.insert("word")
        root.insert("word")

        self.assertTrue(root.find("word"))

    def test_case_sensitive_operations(self):
        root = RadixNode()
        root.insert("Test")

        self.assertTrue(root.find("Test"))
        self.assertFalse(root.find("test"))

    def test_special_characters_in_words(self):
        root = RadixNode()
        root.insert("test@123")

        self.assertTrue(root.find("test@123"))


if __name__ == "__main__":
    unittest.main()
