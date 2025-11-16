"""
System-level test case for Trie data structure.
Tests end-to-end workflow: Dictionary Building and Word Management.
"""

import unittest
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from data_structures.trie.trie import TrieNode


class TestTrieSystemWorkflow(unittest.TestCase):
    """System-level test for Trie dictionary building and word management workflow."""

    def test_dictionary_building_and_word_management_workflow(self):
        """
        Test Case: Dictionary Building and Word Management Workflow

        Pre-conditions: TrieNode initialized

        Test Steps:
        1. Insert multiple related words (apple, application, apply)
        2. Verify all inserted words can be found
        3. Verify non-existent words return False
        4. Delete one word (apple)
        5. Verify deleted word is not found
        6. Verify remaining words still exist

        Expected Results:
        - All inserted words are found successfully
        - Non-inserted words return False
        - After deletion, deleted word returns False
        - Other words remain accessible after deletion
        """
        # Step 1: Initialize Trie and insert words
        trie = TrieNode()
        words_to_insert = ["apple", "application", "apply"]
        trie.insert_many(words_to_insert)

        # Step 2: Verify all inserted words can be found
        for word in words_to_insert:
            self.assertTrue(
                trie.find(word),
                f"Word '{word}' should be found after insertion"
            )

        # Step 3: Verify non-existent words return False
        non_existent_words = ["app", "applicatio", "apples"]
        for word in non_existent_words:
            self.assertFalse(
                trie.find(word),
                f"Word '{word}' should not be found (never inserted)"
            )

        # Step 4: Delete one word
        trie.delete("apple")

        # Step 5: Verify deleted word is not found
        self.assertFalse(
            trie.find("apple"),
            "Word 'apple' should not be found after deletion"
        )

        # Step 6: Verify remaining words still exist
        remaining_words = ["application", "apply"]
        for word in remaining_words:
            self.assertTrue(
                trie.find(word),
                f"Word '{word}' should still be found after deleting 'apple'"
            )


if __name__ == "__main__":
    unittest.main()
