# Security Testing Report

## Test Scope and Coverage
We ran **Bandit** (Python security static analysis) across the following project folders:
- `data_structures/arrays`
- `data_structures/binary_tree`
- `data_structures/disjoint_set`
- `data_structures/hashing`

Targeted vulnerabilities:
- Insecure coding practices (e.g., use of `assert`, unsafe random number generation)
- Misconfigurations or weak constructs

## Vulnerability Summary

| Title | Type | Severity | Recommended Fix |
|-------|------|----------|-----------------|
| Use of `assert` in production code (multiple files) | Misconfiguration / Logic Validation | Low | Replace `assert` with explicit exception handling (e.g., `if not condition: raise ValueError(...)`) |
| Use of `random.choice` for Sudoku solver | Weak Randomness (CWE-330) | Low | Use `secrets.choice` or `SystemRandom` for cryptographic/security-sensitive randomness |
| Lack of input validation in hashing modules | Data Validation | Medium | Add type checks and sanitize inputs before hashing |
| No dependency audit performed | Dependency Vulnerability | Medium | Run `pip-audit` and upgrade any packages with CVEs |


## Execution and Results
- **Tool Used:** Bandit v1.9.1
- **Execution:** `bandit -r data_structures/arrays data_structures/binary_tree data_structures/disjoint_set data_structures/hashing`
- **Results:** Multiple low-severity findings (`assert` misuse), one weak randomness issue (`random.choice`), no high-severity vulnerabilities.
- **Outcome:** Issues documented; recommended fixes provided. No failed scans or unexpected behavior.

## Group Contributions

| Name           | Task / Contribution                                                                 | Notes                                                                 |
|----------------|--------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| Uzair Mukadam  | - Executed Bandit for `arrays`, `binary_tree`, `disjoint_set.py` and `hashing` | Documented `assert` misuse and proposed fixes |
