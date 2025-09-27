import pytest
from data_structures.heap.heap import Heap

def test_empty_heap_extract_max():
    h = Heap()
    with pytest.raises(Exception, match="Empty heap"):
        h.extract_max()

def test_single_element_heap():
    h = Heap()
    h.insert(42)
    assert h.extract_max() == 42
    assert h.h == []

def test_negative_numbers():
    h = Heap()
    h.build_max_heap([-10, -20, -5, -15])
    assert h.extract_max() == -5
    assert h.h[0] <= h.h[1] and h.h[0] <= h.h[2]
