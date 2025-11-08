import io
import sys
import unittest

from data_structures.trie.trie import TrieNode, print_words


class TestTrieEdgeCases(unittest.TestCase):


    def test_delete_edge_cases_and_partial_matches(self) -> None:

        trie = TrieNode()


        words = ["cat", "cats", "dog", "doggy", "door", "do"]
        trie.insert_many(words)


        trie.delete("ca")
        assert trie.find("cat")
        assert trie.find("cats")


        trie.delete("xyz")
        assert trie.find("cat")
        assert trie.find("dog")


        trie.delete("cat")
        assert not trie.find("cat")
        assert trie.find("cats")


        trie.delete("doggy")
        assert not trie.find("doggy")
        assert trie.find("dog")
        assert trie.find("door")


        trie.delete("do")
        assert not trie.find("do")
        assert trie.find("dog")
        assert trie.find("door")


        remaining_words = ["cats", "dog", "door"]
        for word in remaining_words:
            assert trie.find(word), f"Word '{word}' should still exist"

    def test_empty_operations_and_special_characters(self) -> None:

        trie = TrieNode()


        trie.insert("")
        assert trie.find("")
        assert trie.is_leaf


        empty_trie = TrieNode()
        assert not empty_trie.find("")


        special_words = ["hello!", "@symbol", "café", "résumé", "123", "a-b_c"]
        trie.insert_many(special_words)

        for word in special_words:
            assert trie.find(word), f"Special word '{word}' should be found"


        trie.delete("@symbol")
        assert not trie.find("@symbol")
        assert trie.find("hello!")


        trie.insert("CaseSensitive")
        assert trie.find("CaseSensitive")
        assert not trie.find("casesensitive")
        assert not trie.find("CASESENSITIVE")


        test_trie = TrieNode()
        test_trie.insert_many(["a", "ab", "abc"])


        captured_output = io.StringIO()
        sys.stdout = captured_output
        print_words(test_trie, "")
        sys.stdout = sys.__stdout__

        output = captured_output.getvalue()

        assert "a " in output
        assert "ab " in output
        assert "abc " in output


if __name__ == "__main__":
    unittest.main()
