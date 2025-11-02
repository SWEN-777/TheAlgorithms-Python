# 🧼 Static Analysis & Code Smell Detection Report

## 🛠️ Tool Used
- **Tool:** [Ruff](https://docs.astral.sh/ruff/)
- **Version:** 0.14.3
- **Configuration:** Default
- **Directories Scanned:**
  - `data_structures/arrays`
  - `data_structures/binary_tree`
  - `data_structures/disjoint_set`
  - `data_structures/hashing`

---

## 🧪 Static Analysis Results Summary

| Directory        | File Name                                             | Issue Type(s)                             | Count |
|------------------|-------------------------------------------------------|-------------------------------------------|-------|
| disjoint_set     | `disjoint_set.py`                                     | Type annotation quotes (UP037), EOF newline (W292) | 2     |
| disjoint_set     | `test_disjoint_set_mocked.py`                         | Assertion style (PT009), formatting       | 20+   |
| disjoint_set     | `test_alternate_disjoint_set_mocked.py`              | Assertion style (PT009), whitespace (W293), unused imports (F401), naming (N806) | 30+   |
| binary_tree      | `wavelet_tree_edge_tests.py`                         | Unused import (F401), unsorted imports (I001), long line (E501) | 3     |
| arrays           | `sudoku_solver.py`                                    | Unused unpacked variable (RUF059)         | 1     |
| hashing          | `quadratic_probing_mock_test.py`                      | Unused import (F401), unsorted imports (I001) | 2     |

---

## 🔍 Key Findings

- **Assertion Style (PT009):** Over 40 instances of `unittest-style` assertions (`assertEqual`, `assertTrue`, etc.) were replaced with native `assert` statements for clarity and consistency.
- **Whitespace and Formatting (W292, W293, W291):** Multiple files had trailing whitespace, blank lines with spaces, or missing newlines at EOF.
- **Import Hygiene (F401, I001):** Several files had unused imports or disorganized import blocks.
- **Naming Convention (N806):** Uppercase variables like `SRC`, `DST` were renamed to lowercase for PEP8 compliance.
- **Unused Variable (RUF059):** In `sudoku_solver.py`, the unpacked variable `n` was unused and replaced with `_n`.

---

## ✅ Fix Summary

| File                                         | Before                                                                 | After                                                                  |
|----------------------------------------------|------------------------------------------------------------------------|-------------------------------------------------------------------------|
| `disjoint_set.py`                            | `self.parent: "Node" = None`                                           | `self.parent: Node = None`                                             |
| `disjoint_set.py`                            | No newline at EOF                                                      | Added newline                                                          |
| `test_disjoint_set_mocked.py`                | `self.assertEqual(...)`, `self.assertTrue(...)`                        | Replaced with `assert ...`                                             |
| `test_alternate_disjoint_set_mocked.py`      | Unused imports, uppercase vars, trailing whitespace                    | Removed imports, renamed `SRC/DST → src/dst`, cleaned whitespace       |
| `wavelet_tree_edge_tests.py`                 | `import pytest` (unused), long line, unsorted imports                  | Removed `pytest`, split long line, organized imports                   |
| `quadratic_probing_mock_test.py`             | `import pytest` (unused), unsorted imports                             | Removed `pytest`, organized imports                                    |

---

## 👥 Group Contributions

| Name           | Task / Contribution                                                                 | Notes                                                           |
|----------------|--------------------------------------------------------------------------------------|------------------------------------------------------------------|
| Uzair Mukadam  | - Ran Ruff static analysis on arrays, binary_tree, disjoint_set and hashing, and fixed some of the issues | detected over 38 issues and fixed 22 out of it |
| [Teammate 2]   | - Something | Something |
| [Teammate 3]   | - Something | Something |
