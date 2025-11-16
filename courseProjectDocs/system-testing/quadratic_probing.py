import unittest
import subprocess
import sys
import os

from data_structures.hashing.quadratic_probing import QuadraticProbing


class TestSystemLevelHashing(unittest.TestCase):

    def test_insert_single_element(self):
        """Validate inserting a single element end-to-end"""
        qp = QuadraticProbing(5)
        qp.insert_data(10)
        keys = qp.keys()
        self.assertEqual(keys, {0: 10})

    def test_bulk_insert_workflow(self):
        """Validate bulk insertion workflow"""
        qp = QuadraticProbing(5)
        qp.bulk_insert([5, 4, 3, 2, 1])
        keys = qp.keys()
        for val in [5, 4, 3, 2, 1]:
            self.assertIn(val, keys.values())

    def test_collision_resolution(self):
        """Validate collision resolution via quadratic probing"""
        qp = QuadraticProbing(3)
        qp.bulk_insert([17, 18, 99])
        keys = qp.keys()
        for val in [17, 18, 99]:
            self.assertIn(val, keys.values())

    def test_rehashing_trigger(self):
        """Validate rehashing when load factor exceeded"""
        qp = QuadraticProbing(2)
        qp.bulk_insert([10, 20, 30])
        keys = qp.keys()
        for val in [10, 20, 30]:
            self.assertIn(val, keys.values())
        self.assertGreater(qp.size_table, 2)


if __name__ == "__main__":
    unittest.main()
