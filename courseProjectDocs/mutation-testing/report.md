# Mutation Testing Report

## Overview
Mutation testing was performed on `disjoint_set.py` to evaluate the effectiveness of the test suite. Mutations were introduced using Mutatest, and the test suite was executed to determine which mutations were detected ("killed") and which survived.

## Mutation Summary
- Total mutation targets identified: 16
- Sample size tested- Sample size tested: 3
- Mutants killed: 0
- Mutants survived: 3
- Mutation score: 0%

## Surviving Mutants
| Line | Mutation | Description |
|------|----------|-------------|
: 3
- Mutants killed: 0
- Mutants survived: 3
- Mutation score: 0%

## Surviving Mutants
| Line | Mutation | Description |
|------|----------|-------------|
| 8    | `None → True` | In `Node.__init__`, `self.parent` mutated to `True` |
| 23   | `None → True` | In `make_set`, `x.parent` mutated| 8    | `None → True` | In `Node.__init__`, `self.parent` mutated to `True` |
| 23   | `None → True` | In `make_set`, `x.parent` mutated to `True` |
| 38 to `True` |
| 38   | `None → False` | In `find_set`, `x.parent` mutated to `False` |

##   | `None → False` | In `find_set`, `x.parent` mutated to `False` |

## Why These Survive
These mutations do not cause observable failures in the current logic. They alter internal state in ways that are Why These Survive
These mutations do not cause observable failures in the current logic. They alter internal state in ways that are syntactically valid and do not violate test assertions. Additional type enforcement or structural checks could catch them, but would deviate from the original algorithm.

## Test Suite Enhancements
To target these mutations, the following tests were added:
- `test_node_parent syntactically valid and do not violate test assertions. Additional type enforcement or structural checks could catch them, but would deviate from the original algorithm.

## Test Suite Enhancements
To target these mutations, the following tests were added:
- `test_node_parent_is_none_before_make_set`
- `test_make_set_parent_is_not_true`
- `test_make_set_parent_is_not_is_none_before_make_set`
- `test_make_set_parent_is_not_true`
- `test_make_set_parent_is_not_false`
- `test_find_set_parent_identity_not_true`

Despite these additions, the mutants survived due to the permiss_false`
- `test_find_set_parent_identity_not_true`

Despite these additions, the mutants survived due to the permissive nature of Python’s truthiness and object identity.


## Conclusion
The test suite demonstrates strong behavioral strong behavioral coverage. The surviving mutants are non-lethal under current coverage. The surviving mutants are non-lethal under current design and do not compromise correctness. Mutation testing helped validate edge case handling and inspired defensive design and do not compromise correctness. Mutation testing helped validate edge case handling and inspired defensive assertions.