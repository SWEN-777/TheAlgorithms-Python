# Integration Testing Report

## Test Design Summary

We integrated:

- `QuadraticProbing` (subclass of `HashTable`)
- `HashTable` core logic (insertion, collision resolution, rehashing)
- `next_prime` from `number_theory.prime_numbers`

Tested interactions:

- Collision resolution via quadratic probing
- Rehashing triggers prime resize
- Edge case handling with minimal table size
- Type safety for float keys

## Test Data Preparation

- Used `bulk_insert` with values that force collisions and rehashing
- Edge case: table size = 1
- Float key to trigger `TypeError`

## Execution and Results

- Ran tests using `unittest` via `python -m data_structures.hashing.quadratic_probing_integration_testing`
- Verified correct key placement and table resizing

## Bug Reports

- None identified for QuadraticProbing integration

---

## Test Design Summary - Trie and RadixTree Integration

We integrated:

- `TrieNode` from `data_structures.trie.trie` (standard trie/prefix tree implementation)
- `RadixNode` from `data_structures.trie.radix_tree` (space-optimized radix tree/patricia tree)

Tested interactions:

- Consistency of insert, find, and delete operations between both data structures
- Prefix sharing and node compression behavior
- Edge cases: empty strings, single character words, shared prefixes
- Bulk operations with mixed insert/find/delete sequences
- Memory efficiency differences (RadixTree compresses paths, Trie maintains individual character nodes)

## Test Data Preparation - Trie/RadixTree

- Used word sets with common prefixes to test compression: `["banana", "bananas", "bandana", "band"]`
- Edge cases: empty strings, single characters `["a", "b", "c"]`
- Words with long unique suffixes to test RadixTree compression
- Bulk operations with mixed insert/delete sequences on datasets of 10+ words
- Prefix-heavy datasets: `["car", "card", "care", "careful", "carefully"]`

## Execution and Results - Trie/RadixTree

- Ran tests using `unittest` via `python -m unittest data_structures.trie.tests.test_trie_radix_integration -v`
- Verified consistency of operations between Trie and RadixTree
- All 8 tests passed successfully

## Bug Reports - Trie/RadixTree

**Bug identified in RadixTree**: The `find()` method doesn't handle empty strings, raising `IndexError: string index out of range` when `find("")` is called, even though `insert("")` works without error. This is documented in the test case `test_edge_case_empty_string`.

**File:** `data_structures/trie/radix_tree.py`, line 114

```python
def find(self, word: str) -> bool:
    incoming_node = self.nodes.get(word[0], None)  # Fails if word is empty
```

## Group Contributions

- Uzair Mukadam: Designed and implemented all integration tests, debugged failures, and documented results
- Shridhar Vilas Shinde: Designed and implemented integration tests for Trie and RadixTree, debugged failures, identified bug in RadixTree, and documented results

## Group Contributions

| Name                  | Task / Contribution                                                               | Notes                         |
| --------------------- | --------------------------------------------------------------------------------- | ----------------------------- |
| Uzair Mukadam         | Designed and implemented integration tests for quadratic_probing under hashing    | Successfully executed 5 tests |
| Shridhar Vilas Shinde | Designed and implemented integration tests for Trie and RadixTree data structures | Successfully executed 8 tests |
