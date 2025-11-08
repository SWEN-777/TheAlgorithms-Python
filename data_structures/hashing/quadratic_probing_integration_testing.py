import unittest
from .quadratic_probing import QuadraticProbing
from .number_theory.prime_numbers import next_prime


class TestQuadraticProbingIntegration(unittest.TestCase):

    def test_quadratic_collision_resolution(self):
        """Test that quadratic probing resolves collisions correctly"""
        qp = QuadraticProbing(5)
        qp.bulk_insert([0, 3, 6])
        keys = qp.keys()
        self.assertEqual(len(keys), 3)
        self.assertTrue(all(val in [0, 3, 6] for val in keys.values()))

    def test_quadratic_rehashing_triggers_next_prime(self):
        """Test that rehashing uses next_prime correctly"""
        qp = QuadraticProbing(2)
        qp.bulk_insert([10, 20, 30])
        self.assertGreater(qp.size_table, 2)
        self.assertEqual(qp.size_table, next_prime(2, factor=2))

    def test_quadratic_edge_case_size_one(self):
        """Test behavior when initial table size is 1"""
        qp = QuadraticProbing(1)
        qp.bulk_insert([0, 999, 111])
        keys = qp.keys()
        self.assertEqual(len(keys), 2)
        self.assertTrue(all(val in [0, 999, 111] for val in keys.values()))

    def test_quadratic_float_key_failure(self):
        """Test that inserting a float key raises TypeError"""
        qp = QuadraticProbing(3)
        qp.insert_data(10)
        with self.assertRaises(TypeError):
            qp.insert_data(99.99)

    def test_quadratic_balanced_factor_limit(self):
        """Test that probing stops when load factor exceeds limit"""
        qp = QuadraticProbing(2)
        qp.bulk_insert([1, 2])
        self.assertGreaterEqual(qp.balanced_factor(), qp.lim_charge)


if __name__ == "__main__":
    unittest.main()
