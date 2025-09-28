# Environment Setup and Test Report

## Environment Setup

### **Dependencies Installed:**

1. Install requirements for the repository by running the following command:

```bash
pip install -r requirements.txt
```

## Test Report

### Test Suite Summary

The test suite consists of two main testing approaches applied to the **data_structures** folder:

**1. Doctest Framework:**

- **Type**: Unit Testing
- **Purpose**: Tests embedded in docstrings that serve as both documentation and unit tests
- **Execution**: Individual module testing with coverage analysis

**2. Pytest Framework:**

- **Type**: Integration Testing
- **Purpose**: Comprehensive test discovery and execution
- **Execution**: Automated test collection and parallel execution

**Test Results Summary:**

- **Total Doctest Cases**: 1,289 tests executed
- **Passed**: 1,265 tests
- **Failed**: 24 tests

### Coverage Metrics

**Statement Coverage Analysis:**

**Doctest Coverage:**

- **Average Coverage**: 58.9% across all successfully tested modules

**Pytest Coverage:**

- **Average Coverage**: 20% for entire data_structures module

### New Test Cases 

**Changes:** The above coverage metrics has been updated with the new metrics. Overall the number of tests and coverage for the data structures module has increased. The new tests added to  the module include edge cases or missing tests for the following data structures:
- Wavelet Tree
- Heap
- Disjoint Set
- Alternate Disjoint Set
- Priority Queue
- Stack 
- Suffix Tree
- Trie

Note: Both test coverage and result documents (screenshot, pdf) are update

