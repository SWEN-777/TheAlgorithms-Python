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

## Group Contributions
- Uzair Mukadam: Designed and implemented all system-level test cases, executed tests, and documented results.

## Group Contributions

| Name           | Task / Contribution                                                                 | Notes                                                                 |
|----------------|--------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| Uzair Mukadam  | Designed and implemented system-level test cases for `quadratic_probing.py` | Added 4 test cases |