# Mock Strategy

## New Test Cases & Rationale

| Test Case | Purpose |
|-----------|---------|
| Probe lands on third attempt | Simulates multiple collisions before success |
| Probe aborts on full table | Ensures probing halts when load factor is exceeded |
| Probe wraps around table | Validates modulo logic and circular probing |
| Probe finds first available slot | Confirms early success in probing |
| Probe handles negative keys | Tests robustness against negative input |
| Push with mocked deque | Tests queue behavior during push operation |
| Push transfers elements correctly | Verifies elements transfer between queues in correct order |
| Pop from empty raises error | Ensures proper error handling for empty stack |
| Peek on empty returns none | Validates peek behavior on empty stack |
| Interactive menu push | Tests user input simulation for push operation |
| Interactive menu pop | Tests user input simulation for pop operation |
| Interactive menu peek | Tests user input simulation for peek operation |
| Element Initialization Check | Verifies Node initialization using attribute tracking |
| Set Combination with Equal Ranks | Tests the combination process (equal ranks) |
| Set Combination with Unequal Ranks | Tests the combination process (unequal ranks) |
| Path Simplification | Verifies the path optimization process |
| Redundant Set Join | Tests the join process failure (identical reps) |
| Rank Heuristic Join | Tests the join process success |


## Mocking Strategy

### Hash Table
- **`hash_function`**: Mocked to control index mapping and simulate wrap-around.
- **`balanced_factor`**: Mocked to simulate full or sparse table conditions.
- **`values`**: Manually populated to simulate collisions and available slots.

### Stack
- **`deque`**: Mocked to control queue behavior and test internal transfers.
- **`builtins.input`**: Mocked to simulate user input for interactive operations.
- **`builtins.print`**: Mocked to capture console output.

### Disjoint Set
- **`Node`**: Faked using MagicMock(spec=Node) to verify internal attribute assignment (rank, parent).
- **`find_set`**: Mocked  within union_set tests to control the root nodes and their ranks, isolating the union logic.
- **`get_parent`** (Alternate Disjoint Set): Mocked  within merge tests to control the parent indices returned, simplifying the testing of the merge (union-by-rank) logic.

