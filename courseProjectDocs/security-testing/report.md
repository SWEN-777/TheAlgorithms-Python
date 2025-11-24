# Security Testing Report

## Test Scope and Coverage

We ran **Bandit** (Python security static analysis) across the following project folders:

- `data_structures/arrays`
- `data_structures/binary_tree`
- `data_structures/disjoint_set`
- `data_structures/hashing`
- `data_structures/stacks`
- `data_structures/suffix_tree`
- `data_structures/trie`
- `data_structures/linked_list`

Targeted vulnerabilities:

- Insecure coding practices (e.g., use of `assert`, unsafe random number generation)
- Misconfigurations or weak constructs
- Unsafe control flow or input misuse

## Vulnerability Summary

| Title                                               | Type                                          | Severity | Recommended Fix                                                                                                                       |
| --------------------------------------------------- | --------------------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Use of `assert` in production code (multiple files) | Misconfiguration / Logic Validation           | Low      | Replace `assert` with explicit exception handling (e.g., `if not condition: raise ValueError(...)`)                                   |
| Use of `random.choice` for Sudoku solver            | Weak Randomness (CWE-330)                     | Low      | Use `secrets.choice` or `SystemRandom` for cryptographic/security-sensitive randomness                                                |
| Lack of input validation in hashing modules         | Data Validation                               | Medium   | Add type checks and sanitize inputs before hashing                                                                                    |
| No dependency audit performed                       | Dependency Vulnerability                      | Medium   | Run `pip-audit` and upgrade any packages with CVEs                                                                                    |
| Use of `assert` in stack test functions             | Misconfiguration / Logic Validation (CWE-703) | Low      | Replace `assert` statements in test functions with proper test framework assertions (e.g., `self.assertTrue()`, `self.assertEqual()`) |
| Use of `assert` in suffix tree test cases           | Misconfiguration / Logic Validation (CWE-703) | Low      | Use unittest assertion methods instead of bare `assert` statements                                                                    |
| Use of `assert` in trie validation logic            | Misconfiguration / Logic Validation (CWE-703) | Low      | Replace `assert` with explicit validation using unittest methods or proper exception handling                                         |
| Use of `assert` in CircularLinkedList implementation            | Misconfiguration / Logic Validation (CWE-703) | Low      |Replace with explicit error handling, as asserts are stripped in optimized mode and unsafe for runtime validation                                         |

## Execution and Results

- **Tool Used:** Bandit v1.9.1
- **Execution:**
  - Uzair: `bandit -r data_structures/arrays data_structures/binary_tree data_structures/disjoint_set data_structures/hashing`
  - Shridhar: `bandit -r data_structures/stacks data_structures/suffix_tree data_structures/trie `
  - Rohini: `bandit -r data_structures/linked_list`
- **Results:**
  - Uzair's scan: Multiple low-severity findings (`assert` misuse), one weak randomness issue (`random.choice`), no high-severity vulnerabilities.
  - Shridhar's scan: 160 low-severity issues (all `assert` usage), 2761 lines of code scanned, no medium or high-severity vulnerabilities.
  - Rohini's scan: CircularLinkedList reported several unsafe assert uses in traversal and length validation
- **Outcome:** Issues documented; recommended fixes provided. No failed scans or unexpected behavior.

## Group Contributions

| Name            | Task / Contribution                                                        | Notes                                                           |
| --------------- | -------------------------------------------------------------------------- | --------------------------------------------------------------- |
| Uzair Mukadam   | Executed Bandit for `arrays`, `binary_tree`, `disjoint_set`, and `hashing` | Documented `assert` misuse, weak randomness, and proposed fixes |
| Shridhar Shinde | Executed Bandit for `stacks`, `suffix_tree`, and `trie`                    | Documented 160 `assert` usage issues across 3 data structures   |
| Rohini Senthilkumar | Executed Bandit for `linked_list`                    | Identified 34 unsafe assert usages in CircularLinkedList traversal, insertion, deletion, and length validation logic   |
