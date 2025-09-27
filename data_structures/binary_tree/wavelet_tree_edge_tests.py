import pytest
from data_structures.binary_tree.wavelet_tree import build_tree, rank, rank_till_index, quantile, range_counting

def test_empty_array():
    root = build_tree([])
    assert root is None
    assert rank(root, 1, 0, 0) == 0
    assert rank_till_index(root, 1, 0) == 0
    assert quantile(root, 0, 0, 0) == -1
    assert range_counting(root, 0, 0, 0, 10) == 0

def test_single_element_array():
    root = build_tree([5])
    assert root.minn == 5 and root.maxx == 5
    assert rank(root, 5, 0, 0) == 1
    assert rank_till_index(root, 5, 0) == 1
    assert quantile(root, 0, 0, 0) == 5
    assert range_counting(root, 0, 0, 0, 10) == 1

def test_query_nonexistent_value():
    root = build_tree([1, 2, 3, 4])
    assert rank(root, 99, 0, 3) == 0
    assert rank_till_index(root, 99, 3) == 0
    assert range_counting(root, 0, 3, 100, 200) == 0
