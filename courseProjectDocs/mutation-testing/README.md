# Mutation Testing Setup

## Project Context
This assignment applies mutation testing to data structues using the Mutatest tool. The goal is to evaluate the robustness of the test suite by introducing small code mutations and observing whether the tests detect them.

## Tool Used
- [Mutatest](https://pypi.org/project/mutatest/)
- Python 3.13.2
- Pytest 8.4.2

## How to Run Mutation Tests

1. Install dependencies:
```bash
pip install mutatest pytest
```

2. Run mutation testing:
```bash
mutatest -s data_structures/disjoint_set/disjoint_set.py \
         -t "pytest data_structures/disjoint_set/test_disjoint_set_mocked.py" \
         -m s --parallel --timeout_factor 2.0
```

## Target Files

- data_structures/disjoint_set/disjoint_set.py

## Test Files

- data_structures/disjoint_set/test_disjoint_set_mocked.py

## Notes

- Python 3.13 introduced stricter behavior for random.sample() on sets. Mutatest was patched locally to convert sets to sorted lists.

- All tests pass cleanly before mutation trials.


## Group Contributions

| Name           | Task / Contribution                                                                 | Notes                                                                 |
|----------------|--------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| Uzair Mukadam  | - Implemented and debugged mutation testing on `disjoint_set.py` using Mutatest | Targeted 3 surviving mutants with focused tests |

