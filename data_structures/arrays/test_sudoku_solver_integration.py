import pytest
import time
from data_structures.arrays.sudoku_solver import (
    solve, solved, grid1, grid2, parse_grid, digits, rows, cols, squares, assign, eliminate, units,
    search
)

# --- Integration Test Group: Full Solve Cycle ---

def test_full_solve_integration_grid1():
    """
    Test the integration of parse_grid -> search -> solve on a standard puzzle.
    """
    solution_values = solve(grid1)

    # 1. Integration check: Did the solver produce a result?
    assert solution_values is not False

    # 2. Integration check: Is the result valid according to the unit rules?
    assert solved(solution_values) is True

    # 3. Simple length check for robustness
    assert len(solution_values) == 81

def test_full_solve_integration_grid2():
    """
    Test the full solve integration on a second, different puzzle.
    """
    solution_values = solve(grid2)

    assert solution_values is not False
    assert solved(solution_values) is True

def test_solve_integration_with_empty_grid():
    """
    Test the integration on a completely empty 9x9 grid.
    We only check that a valid solution is found, as the specific digits are non-deterministic.
    """
    empty_grid = '.' * 81
    solution_values = solve(empty_grid)

    assert solution_values is not False
    assert solved(solution_values) is True
    
    # FIX 2: Removed specific digit checks (e.g., assert '2' in solution_values['B2'])
    # The solved(solution_values) check is sufficient for non-deterministic results.


# --- Integration Test Group: Constraint Propagation (Assign/Eliminate) ---

def test_assign_eliminate_propagation():
    """
    Tests the core constraint propagation integration by assigning one value
    and verifying its elimination in a peer.
    """
    test_grid = "." * 81 # Start with empty grid
    values = parse_grid(test_grid)

    # Assign '2' to A2. This eliminates '2' from all 20 peers.
    result = assign(values.copy(), 'A2', '2')

    # 1. Verify self-propagation (assign and eliminate integration)
    assert result is not False
    assert result['A2'] == '2'

    # 2. Check elimination on a row peer (A3)
    assert '2' not in result['A3']

    # 3. Check elimination on a 3x3 block peer (B1)
    assert '2' not in result['B1']

def test_elimination_rule_2_integration():
    """
    Tests the critical integration of Rule 2: 'single place in unit' logic
    that forces an assignment (using the integration of eliminate and assign).
    """
    # FIX 3: Simplified the setup to isolate Rule 2 in the A1-C3 block unit.
    values_r2 = parse_grid("." * 81)
    
    # Eliminate '1' from every square in the A1-C3 block unit EXCEPT A1.
    block_unit = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
    for s in block_unit:
        if s != 'A1':
             # The result of the intermediate elimination is ignored.
             eliminate(values_r2, s, '1')

    # Now, '1' is only possible in A1 in that block unit. Rule 2 should have triggered assign(A1, '1').
    assert values_r2['A1'] == '1'
    # Verify Rule 1 (assignment propagation) ran after Rule 2's assignment
    assert '1' not in values_r2['A4'] 

