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
- data_structures/stacks/stack_using_two_queues.py

## Test Files

- data_structures/disjoint_set/test_disjoint_set_mocked.py
- data_structures/stacks/test_stack_mutation.py

## Stack Mutation Testing

1. Run mutation testing on Stack implementation:
```bash
mutatest -s data_structures/stacks/stack_using_two_queues.py \
         -t "pytest data_structures/stacks/test_stack_mutation.py" \
         -m s --parallel --timeout_factor 2.0
```

2. The stack implementation has 23 total mutation targets identified by Mutatest

3. Tests cover all behavioral mutations in push, pop, and peek methods

## Notes

- Python 3.13 introduced stricter behavior for random.sample() on sets. Mutatest was patched locally to convert sets to sorted lists.

- Python 3.12 also has the same issue with random.sample() on sets. The fix involves converting sets to lists in mutatest/run.py line 530.

- All tests pass cleanly before mutation trials.


## Group Contributions

| Name           | Task / Contribution                                                                 | Notes                                                                 |
|----------------|--------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| Uzair Mukadam  | - Implemented and debugged mutation testing on `disjoint_set.py` using Mutatest | Targeted 3 surviving mutants with focused tests |
| Shridhar Shinde| - Implemented mutation testing on `stack_using_two_queues.py` using Mutatest | Created comprehensive test suite targeting type annotation and behavioral mutations |

