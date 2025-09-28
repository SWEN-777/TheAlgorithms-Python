import unittest
from data_structures.stacks.stock_span_problem import calculate_span


class TestStockSpanEdgeCases(unittest.TestCase):
    

    def test_empty_and_single_element_arrays(self) -> None:
       
        
        result_empty = calculate_span([])
        self.assertEqual(result_empty, [])
        self.assertEqual(len(result_empty), 0)

        
        result_single = calculate_span([42])
        self.assertEqual(result_single, [1])
        self.assertEqual(len(result_single), 1)

        
        result_identical = calculate_span([5, 5])
        self.assertEqual(result_identical, [1, 2])

        
        result_desc = calculate_span([10, 5])
        self.assertEqual(result_desc, [1, 1])

        
        result_asc = calculate_span([5, 10])
        self.assertEqual(result_asc, [1, 2])

    def test_extreme_values_and_patterns(self) -> None:
       
        
        identical_values = [100] * 5
        result_flat = calculate_span(identical_values)
        expected_flat = [1, 2, 3, 4, 5]  
        self.assertEqual(result_flat, expected_flat)

        
        zero_values = [0, 0, 0, 0]
        result_zeros = calculate_span(zero_values)
        expected_zeros = [1, 2, 3, 4]
        self.assertEqual(result_zeros, expected_zeros)

        
        large_values = [1000000, 2000000, 1500000, 3000000]
        result_large = calculate_span(large_values)
        expected_large = [1, 2, 1, 4]
        self.assertEqual(result_large, expected_large)

        
        alternating = [100, 50, 200, 25, 300]
        result_alt = calculate_span(alternating)
        expected_alt = [1, 1, 3, 1, 5]  
        self.assertEqual(result_alt, expected_alt)

        
        negative_values = [-10, -5, -15, -2]
        result_negative = calculate_span(negative_values)
        expected_negative = [1, 2, 1, 4]
        self.assertEqual(result_negative, expected_negative)

       
        v_pattern = [50, 20, 10, 30, 60]
        result_v = calculate_span(v_pattern)
        expected_v = [1, 1, 1, 4, 5]
        self.assertEqual(result_v, expected_v)


if __name__ == "__main__":
    unittest.main()