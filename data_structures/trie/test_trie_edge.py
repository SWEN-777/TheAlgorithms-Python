import unittest
from data_structures.trie.trie import TrieNode, print_words
import io
import sys


class TestTrieEdgeCases(unittest.TestCase):
   

    def test_delete_edge_cases_and_partial_matches(self) -> None:
        
        trie = TrieNode()

        
        words = ["cat", "cats", "dog", "doggy", "door", "do"]
        trie.insert_many(words)

       
        trie.delete("ca")  
        self.assertTrue(trie.find("cat"))
        self.assertTrue(trie.find("cats"))

        
        trie.delete("xyz") 
        self.assertTrue(trie.find("cat"))
        self.assertTrue(trie.find("dog"))

        
        trie.delete("cat") 
        self.assertFalse(trie.find("cat"))
        self.assertTrue(trie.find("cats"))  

        
        trie.delete("doggy")  
        self.assertFalse(trie.find("doggy"))
        self.assertTrue(trie.find("dog"))
        self.assertTrue(trie.find("door"))  

        
        trie.delete("do")
        self.assertFalse(trie.find("do"))
        self.assertTrue(trie.find("dog"))  
        self.assertTrue(trie.find("door"))

        
        remaining_words = ["cats", "dog", "door"]
        for word in remaining_words:
            self.assertTrue(trie.find(word), f"Word '{word}' should still exist")

    def test_empty_operations_and_special_characters(self) -> None:
        
        trie = TrieNode()

       
        trie.insert("")  
        self.assertTrue(trie.find(""))  
        self.assertTrue(trie.is_leaf)  

        
        empty_trie = TrieNode()
        self.assertFalse(empty_trie.find(""))  

        
        special_words = ["hello!", "@symbol", "café", "résumé", "123", "a-b_c"]
        trie.insert_many(special_words)

        for word in special_words:
            self.assertTrue(trie.find(word), f"Special word '{word}' should be found")

        
        trie.delete("@symbol")
        self.assertFalse(trie.find("@symbol"))
        self.assertTrue(trie.find("hello!")) 

        
        trie.insert("CaseSensitive")
        self.assertTrue(trie.find("CaseSensitive"))
        self.assertFalse(trie.find("casesensitive"))
        self.assertFalse(trie.find("CASESENSITIVE"))

       
        test_trie = TrieNode()
        test_trie.insert_many(["a", "ab", "abc"])

        
        captured_output = io.StringIO()
        sys.stdout = captured_output
        print_words(test_trie, "")
        sys.stdout = sys.__stdout__

        output = captured_output.getvalue()
       
        self.assertIn("a ", output)
        self.assertIn("ab ", output)
        self.assertIn("abc ", output)


if __name__ == "__main__":
    unittest.main()