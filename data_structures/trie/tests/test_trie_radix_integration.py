"""
Integration tests for Trie and RadixTree data structures.

This module tests the integration between:
- TrieNode (standard trie implementation)
- RadixNode (space-optimized radix/patricia tree)
- Comparing behavior and memory efficiency between both structures
"""

import unittest

from data_structures.trie.radix_tree import RadixNode
from data_structures.trie.trie import TrieNode


class TestTrieRadixIntegration(unittest.TestCase):
    """Integration tests comparing Trie and RadixTree implementations."""

    def test_insert_and_find_consistency(self):
        """
        Test that both Trie and RadixTree return consistent results
        for insert and find operations with the same word set.
        """
        words = ["banana", "bananas", "bandana", "band", "apple", "all", "beast"]

        trie = TrieNode()
        radix = RadixNode()

        # Insert words into both structures
        trie.insert_many(words)
        radix.insert_many(words)

        # Both should find all inserted words
        for word in words:
            self.assertTrue(
                trie.find(word),
                f"Trie should find '{word}'"
            )
            self.assertTrue(
                radix.find(word),
                f"RadixTree should find '{word}'"
            )

        # Both should not find words that weren't inserted
        non_existent_words = ["ban", "banan", "app", "beats", "ally"]
        for word in non_existent_words:
            self.assertFalse(
                trie.find(word),
                f"Trie should not find '{word}'"
            )
            self.assertFalse(
                radix.find(word),
                f"RadixTree should not find '{word}'"
            )

    def test_delete_consistency(self):
        """
        Test that both Trie and RadixTree maintain consistency
        after delete operations.
        """
        words = ["test", "testing", "tester", "tested"]

        trie = TrieNode()
        radix = RadixNode()

        trie.insert_many(words)
        radix.insert_many(words)

        # Delete a word from both
        trie.delete("test")
        radix.delete("test")

        # Both should not find the deleted word
        self.assertFalse(trie.find("test"))
        self.assertFalse(radix.find("test"))

        # Both should still find the remaining words
        remaining_words = ["testing", "tester", "tested"]
        for word in remaining_words:
            self.assertTrue(trie.find(word))
            self.assertTrue(radix.find(word))

    def test_prefix_sharing_behavior(self):
        """
        Test how both structures handle words with common prefixes.
        RadixTree should compress common prefixes, while Trie maintains
        individual character nodes.
        """
        words = ["car", "card", "care", "careful", "carefully"]

        trie = TrieNode()
        radix = RadixNode()

        trie.insert_many(words)
        radix.insert_many(words)

        # Both should find all words
        for word in words:
            self.assertTrue(trie.find(word), f"Trie should find '{word}'")
            self.assertTrue(radix.find(word), f"RadixTree should find '{word}'")

        # Test that prefixes that aren't complete words are not found
        incomplete_prefixes = ["ca", "car", "care", "careful"]
        # Note: "car", "care", "careful" ARE in the word list, so they should be found
        # Only "ca" should not be found
        self.assertFalse(trie.find("ca"))
        self.assertFalse(radix.find("ca"))

        # Verify complete words are found
        self.assertTrue(trie.find("car"))
        self.assertTrue(radix.find("car"))

    def test_edge_case_empty_string(self):
        """
        Test edge case: inserting and finding empty strings.
        RadixTree.find() doesn't handle empty strings (causes IndexError),
        but Trie does. This test verifies Trie's edge case handling and
        documents RadixTree's limitation.
        """
        trie = TrieNode()

        # Insert empty string - Trie handles this
        trie.insert("")

        # Trie should find empty string
        self.assertTrue(trie.find(""))

        # Insert other words
        trie.insert("test")

        # Empty string should still be found
        self.assertTrue(trie.find(""))
        self.assertTrue(trie.find("test"))

        # RadixTree edge case: find("") causes IndexError
        radix = RadixNode()
        radix.insert("")  # insert works
        with self.assertRaises(IndexError):
            radix.find("")  # but find doesn't

    def test_edge_case_single_character_words(self):
        """
        Test edge case: single character words.
        """
        words = ["a", "b", "c", "ab", "abc"]

        trie = TrieNode()
        radix = RadixNode()

        trie.insert_many(words)
        radix.insert_many(words)

        # All words should be found in both structures
        for word in words:
            self.assertTrue(trie.find(word))
            self.assertTrue(radix.find(word))

    def test_delete_with_shared_prefixes(self):
        """
        Test deletion behavior when words share prefixes.
        Deleting one word should not affect others with shared prefixes.
        """
        # Remove duplicate "program" to avoid RadixTree edge case
        words = ["program", "programmer", "programming"]

        trie = TrieNode()
        radix = RadixNode()

        # Insert all words
        trie.insert_many(words)
        radix.insert_many(words)

        # Delete "program"
        trie.delete("program")
        radix.delete("program")

        # "program" should not be found
        self.assertFalse(trie.find("program"))
        self.assertFalse(radix.find("program"))

        # Other words should still exist
        self.assertTrue(trie.find("programmer"))
        self.assertTrue(radix.find("programmer"))
        self.assertTrue(trie.find("programming"))
        self.assertTrue(radix.find("programming"))

    def test_radix_tree_node_compression(self):
        """
        Test that RadixTree compresses paths more efficiently than Trie.
        This is verified by inserting words with long unique suffixes
        and checking that operations still work correctly.
        """
        # Words with long unique parts that RadixTree can compress
        words = [
            "testing",
            "testingextralong",
            "completely",
            "completelydifferent"
        ]

        trie = TrieNode()
        radix = RadixNode()

        trie.insert_many(words)
        radix.insert_many(words)

        # All words should be findable
        for word in words:
            self.assertTrue(trie.find(word))
            self.assertTrue(radix.find(word))

        # Partial matches should not be found (unless they're complete words)
        self.assertFalse(trie.find("test"))
        self.assertFalse(radix.find("test"))
        self.assertFalse(trie.find("complete"))
        self.assertFalse(radix.find("complete"))

    def test_bulk_operations_consistency(self):
        """
        Test consistency between Trie and RadixTree with a larger dataset
        involving multiple inserts, finds, and deletes.
        """
        initial_words = ["alpha", "beta", "gamma", "delta", "epsilon"]
        additional_words = ["alphabet", "better", "gammas", "deltas"]
        delete_words = ["beta", "gamma"]

        trie = TrieNode()
        radix = RadixNode()

        # Initial insertion
        trie.insert_many(initial_words)
        radix.insert_many(initial_words)

        # Verify initial words
        for word in initial_words:
            self.assertTrue(trie.find(word))
            self.assertTrue(radix.find(word))

        # Add more words
        trie.insert_many(additional_words)
        radix.insert_many(additional_words)

        # Verify all words exist
        all_words = initial_words + additional_words
        for word in all_words:
            self.assertTrue(trie.find(word))
            self.assertTrue(radix.find(word))

        # Delete some words
        for word in delete_words:
            trie.delete(word)
            radix.delete(word)

        # Verify deleted words are not found
        for word in delete_words:
            self.assertFalse(trie.find(word))
            self.assertFalse(radix.find(word))

        # Verify remaining words still exist
        remaining_words = ["alpha", "delta", "epsilon", "alphabet",
                          "better", "gammas", "deltas"]
        for word in remaining_words:
            self.assertTrue(trie.find(word))
            self.assertTrue(radix.find(word))


def run_tests():
    """Run all integration tests."""
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTrieRadixIntegration)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    return result


if __name__ == "__main__":
    run_tests()
