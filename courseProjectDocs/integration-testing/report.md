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

## Group Contributions
- Uzair Mukadam: Designed and implemented all integration tests, debugged failures, and documented results

## Group Contributions

| Name           | Task / Contribution                                                                 | Notes                                                                 |
|----------------|--------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| Uzair Mukadam  | Designed and implemented integration tests for quadratic_probing under hashing | Successfully executed 5 tests |
