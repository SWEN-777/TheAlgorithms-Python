# System Testing Report

## Test Scope and Coverage
System tests validate the main workflows of the hashing application:
- Insertion of single elements
- Bulk insertion workflow
- Collision resolution via quadratic probing
- Rehashing when load factor exceeds threshold

## Test Case Summary

| Title | Pre-conditions | Test Steps | Expected Results |
|-------|----------------|------------|------------------|
| Insert Single Element | HashTable initialized with size 5 | Insert value `10`, call `keys()` | Keys = `{0: 10}` |
| Bulk Insert Workflow | HashTable initialized with size 5 | Bulk insert `[5,4,3,2,1]`, call `keys()` | All values present in keys |
| Collision Resolution | HashTable initialized with size 3 | Bulk insert `[17,18,99]`, call `keys()` | All values stored despite collisions |
| Rehashing Trigger | HashTable initialized with size 2 | Bulk insert `[10,20,30]`, call `keys()` | Table size increases, all values preserved |

## Execution and Results
- All system tests executed successfully using `unittest`.
- Bulk insert distributed values correctly.
- Collision resolution worked as expected.
- Rehashing increased table size using `next_prime`.
- No behavioral deviations observed.

---

## Test Scope and Coverage - Trie Data Structure
System tests validate the main workflows of the Trie data structure:
- Dictionary building and word management using Trie
- Word insertion and bulk operations
- Word lookup and validation
- Word deletion while preserving related words

## Test Case Summary - Trie

| Title | Pre-conditions | Test Steps | Expected Results |
|-------|----------------|------------|------------------|
| Dictionary Building and Word Management | TrieNode initialized | 1. Insert words `[apple, application, apply]` 2. Verify all words found 3. Verify non-existent words return False 4. Delete `apple` 5. Verify deletion 6. Verify remaining words exist | All insertions successful, lookups return correct values, deletion removes word while preserving others |

## Execution and Results - Trie
- System test executed successfully using `unittest`.
- Trie word insertion, lookup, and deletion operations performed correctly.
- Prefix relationships maintained correctly (deleting 'apple' did not affect 'application' or 'apply').
- No behavioral deviations observed.

---

## Group Contributions
- Uzair Mukadam: Designed and implemented system-level test cases for `quadratic_probing.py`, executed tests, and documented results.
- Shridhar Shinde: Designed and implemented system-level test case for `trie.py`, executed tests, and documented results.

| Name           | Task / Contribution                                                                 | Notes                                                                 |
|----------------|--------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| Uzair Mukadam  | Designed and implemented system-level test cases for `quadratic_probing.py` | Added 4 test cases |
| Shridhar Shinde  | Designed and implemented system-level test case for `trie.py` | Added 1 test case |