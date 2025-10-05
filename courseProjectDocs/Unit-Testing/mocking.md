# Mock Strategy

## New Test Cases & Rationale

| Test Case | Purpose |
|-----------|---------|
| Probe lands on third attempt | Simulates multiple collisions before success |
| Probe aborts on full table | Ensures probing halts when load factor is exceeded |
| Probe wraps around table | Validates modulo logic and circular probing |
| Probe finds first available slot | Confirms early success in probing |
| Probe handles negative keys | Tests robustness against negative input |

## Mocking Strategy

- **`hash_function`**: Mocked to control index mapping and simulate wrap-around.
- **`balanced_factor`**: Mocked to simulate full or sparse table conditions.
- **`values`**: Manually populated to simulate collisions and available slots.
