import pytest
from unittest.mock import MagicMock
from data_structures.hashing.quadratic_probing import QuadraticProbing

def test_probe_lands_on_third_attempt():
    qp = QuadraticProbing(7)
    qp.values = [None] * 7
    qp.hash_function = MagicMock(side_effect=lambda x: x % 7)
    qp.balanced_factor = MagicMock(return_value=0.5)

    qp.values[1] = "occupied"
    qp.values[4] = "occupied"
    qp.values[2] = None

    result = qp._collision_resolution(0)
    assert result == 2

def test_probe_aborts_on_full_table():
    qp = QuadraticProbing(3)
    qp.values = ["A", "B", "C"]
    qp.hash_function = MagicMock(side_effect=lambda x: x % 3)
    qp.balanced_factor = MagicMock(return_value=0.9)

    result = qp._collision_resolution(0)
    assert result is None

def test_probe_wraps_around_table():
    qp = QuadraticProbing(5)
    qp.values = [None] * 5
    qp.hash_function = MagicMock(side_effect=lambda x: x % 5)
    qp.balanced_factor = MagicMock(return_value=0.3)

    qp.values[1] = "occupied"
    qp.values[4] = "occupied"
    qp.values[2] = "occupied"
    qp.values[0] = "occupied"
    qp.values[3] = None

    result = qp._collision_resolution(0)
    assert result == 3

def test_probe_finds_first_available_slot():
    qp = QuadraticProbing(10)
    qp.values = [None] * 10
    qp.hash_function = MagicMock(side_effect=lambda x: x % 10)
    qp.balanced_factor = MagicMock(return_value=0.2)

    qp.values[1] = "occupied"
    qp.values[4] = None

    result = qp._collision_resolution(0)
    assert result == 4

def test_probe_handles_negative_keys():
    qp = QuadraticProbing(7)
    qp.values = [None] * 7
    qp.hash_function = MagicMock(side_effect=lambda x: abs(x) % 7)
    qp.balanced_factor = MagicMock(return_value=0.1)

    result = qp._collision_resolution(-5)
    assert result is not None and isinstance(result, int)
