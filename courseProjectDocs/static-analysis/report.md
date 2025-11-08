# Static Analysis & Code Smell Detection Report

## Tool Used

- **Tool:** [Ruff](https://docs.astral.sh/ruff/)
- **Version:** 0.14.3
- **Configuration:** Default
- **Directories Scanned:**
  - `data_structures/arrays`
  - `data_structures/binary_tree`
  - `data_structures/disjoint_set`
  - `data_structures/hashing`
  - `data_structures/trie`
  - `data_structures/suffix_tree`

---

## Static Analysis Results Summary

| Directory    | File Name                               | Issue Type(s)                                                                    | Count |
| ------------ | --------------------------------------- | -------------------------------------------------------------------------------- | ----- |
| disjoint_set | `disjoint_set.py`                       | Type annotation quotes (UP037), EOF newline (W292)                               | 2     |
| disjoint_set | `test_disjoint_set_mocked.py`           | Assertion style (PT009), formatting                                              | 20+   |
| disjoint_set | `test_alternate_disjoint_set_mocked.py` | Assertion style (PT009), whitespace (W293), unused imports (F401), naming (N806) | 30+   |
| binary_tree  | `wavelet_tree_edge_tests.py`            | Unused import (F401), unsorted imports (I001), long line (E501)                  | 3     |
| arrays       | `sudoku_solver.py`                      | Unused unpacked variable (RUF059)                                                | 1     |
| hashing      | `quadratic_probing_mock_test.py`        | Unused import (F401), unsorted imports (I001)                                    | 2     |
| trie         | `radix_tree.py`                         | Unused unpacked variable (RUF059)                                                | 2     |
| trie         | `test_radix_tree_mock.py`               | Assertion style (PT009), unused imports (F401), unsorted imports (I001)          | 50+   |
| trie         | `test_trie_edge.py`                     | Assertion style (PT009)                                                          | 51    |
| suffix_tree      | `test_suffix_tree_edge.py`               | Assertion style (PT009), long line (E501), unused loop variable (B007)                         | 20+   |
| suffix_tree      | `test_suffix_tree_mock.py`               | Assertion style (PT009), unused variable (F841), unused argument (ARG002)                      | 30+   |
---

## 🔍 Key Findings

- **Assertion Style (PT009):** Over 40 instances of `unittest-style` assertions (`assertEqual`, `assertTrue`, etc.) were replaced with native `assert` statements for clarity and consistency.
- **Whitespace and Formatting (W292, W293, W291):** Multiple files had trailing whitespace, blank lines with spaces, or missing newlines at EOF.
- **Import Hygiene (F401, I001):** Several files had unused imports or disorganized import blocks.
- **Naming Convention (N806):** Uppercase variables like `SRC`, `DST` were renamed to lowercase for PEP8 compliance.
- **Unused Variable (RUF059):** In `sudoku_solver.py`, the unpacked variable `n` was unused and replaced with `_n`.
- **Trie Module (103 issues):** Comprehensive analysis of the trie data structure revealed 103 code quality issues. The most significant findings include:
  - 101 unittest-style assertions across `test_radix_tree_mock.py` and `test_trie_edge.py` converted to native Python `assert` statements
  - 2 instances of unused unpacked variable `matching_string` in `radix_tree.py` (in `find()` and `delete()` methods) renamed to `_matching_string`
  - Removed unused imports (`Mock`, `MagicMock`, `call` from unittest.mock) in `test_radix_tree_mock.py`
  - Reorganized import statements for better code organization
- **Suffix Tree Module (75 issues):**
  - Unified test assertion style to native `assert` statements.
  - Split long lines exceeding 88 characters for readability.
  - Replaced unused loop variables (`for i in range(len(...))`) with `_` or list comprehensions.
  - Removed unused variables (`temp_result`, `expected_value`) and unused arguments in mock tests.
  - Improved import order and added missing EOF newline for consistency.

---

## Fix Summary

| File                                    | Before                                                                | After                                                                                               |
| --------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `disjoint_set.py`                       | `self.parent: "Node" = None`                                          | `self.parent: Node = None`                                                                          |
| `disjoint_set.py`                       | No newline at EOF                                                     | Added newline                                                                                       |
| `test_disjoint_set_mocked.py`           | `self.assertEqual(...)`, `self.assertTrue(...)`                       | Replaced with `assert ...`                                                                          |
| `test_alternate_disjoint_set_mocked.py` | Unused imports, uppercase vars, trailing whitespace                   | Removed imports, renamed `SRC/DST → src/dst`, cleaned whitespace                                    |
| `wavelet_tree_edge_tests.py`            | `import pytest` (unused), long line, unsorted imports                 | Removed `pytest`, split long line, organized imports                                                |
| `quadratic_probing_mock_test.py`        | `import pytest` (unused), unsorted imports                            | Removed `pytest`, organized imports                                                                 |
| `radix_tree.py`                         | `matching_string, remaining_prefix, remaining_word = ...`             | `_matching_string, remaining_prefix, remaining_word = ...`                                          |
| `test_radix_tree_mock.py`               | `self.assertEqual(...)`, `self.assertIn(...)`, `self.assertTrue(...)` | Replaced with `assert ...`, removed unused imports (`Mock`, `MagicMock`, `call`), organized imports |
| `test_trie_edge.py`                     | `self.assertTrue(...)`, `self.assertFalse(...)`, `self.assertIn(...)` | Replaced with `assert ...`, `assert not ...`, `assert ... in ...`                                   |
 `test_suffix_tree_edge.py`              | `self.assertEqual(...)`, long lines, unused loop variable (`for i`)   | Replaced with native `assert`, split long lines, renamed loop var to `_`                            |
| `test_suffix_tree_mock.py`              | `self.assertTrue(...)`, unused variable (`temp_result`), unused args  | Replaced with native `assert`, removed unused vars, cleaned imports                                 |

---

## Group Contributions

| Name                  | Task / Contribution                                                                                       | Notes                                                 |
| --------------------- | --------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| Uzair Mukadam         | - Ran Ruff static analysis on arrays, binary_tree, disjoint_set and hashing, and fixed some of the issues | detected over 38 issues and fixed 22 out of it        |
| Shridhar Vilas Shinde | - Ran Ruff static analysis on trie data structure and fixed the issues                                    | detected 103 issues (36 safe fixes + 67 unsafe fixes) |
| Rohini Senthilkumar      | - Conducted static analysis on suffix_tree and implemented fixes for assertion and loop issues           | Detected 75 issues, fixed 75                         |
