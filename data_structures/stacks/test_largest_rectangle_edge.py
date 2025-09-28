import unittest
from data_structures.stacks.largest_rectangle_histogram import largest_rectangle_area


class TestLargestRectangleEdgeCases(unittest.TestCase):
    

    def test_empty_and_minimal_arrays(self) -> None:
        
        # Test with empty array
        result_empty = largest_rectangle_area([])
        self.assertEqual(result_empty, 0)

        # Test with array of all zeros
        result_zeros = largest_rectangle_area([0, 0, 0, 0])
        self.assertEqual(result_zeros, 0)

        # Test with single zero
        result_single_zero = largest_rectangle_area([0])
        self.assertEqual(result_single_zero, 0)

        # Test with mix of zeros and non-zeros
        result_mixed_zeros = largest_rectangle_area([0, 3, 0, 4, 0])
        self.assertEqual(result_mixed_zeros, 4) 

        # Test with leading and trailing zeros
        result_edge_zeros = largest_rectangle_area([0, 0, 5, 5, 0, 0])
        self.assertEqual(result_edge_zeros, 10)  

    def test_extreme_patterns_and_values(self) -> None:
        
        
        decreasing = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        result_decreasing = largest_rectangle_area(decreasing)
        self.assertEqual(result_decreasing, 25)  

        
        increasing = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result_increasing = largest_rectangle_area(increasing)
        self.assertEqual(result_increasing, 25)  

        
        identical = [7, 7, 7, 7, 7]
        result_identical = largest_rectangle_area(identical)
        self.assertEqual(result_identical, 35)  

        
        mountain = [1, 2, 10, 10, 10, 2, 1]
        result_mountain = largest_rectangle_area(mountain)
        self.assertEqual(result_mountain, 30)  

        # Test with valley pattern (high-low-high)
        valley = [8, 8, 1, 1, 1, 8, 8]
        result_valley = largest_rectangle_area(valley)
        self.assertEqual(result_valley, 16)  

        # Test with single tall bar surrounded by short bars
        single_tall = [1, 1, 100, 1, 1]
        result_single_tall = largest_rectangle_area(single_tall)
        self.assertEqual(result_single_tall, 100)  

        # Test with large values to ensure no overflow issues
        large_values = [1000000, 1000000]
        result_large = largest_rectangle_area(large_values)
        self.assertEqual(result_large, 2000000) 


if __name__ == "__main__":
    unittest.main()