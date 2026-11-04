import unittest

from search_algorithms.intentional_bugs import (
    binary_search_off_by_one,
    duplicated_linear_scan,
    duplicated_linear_scan_again,
    interpolation_search_divide_by_zero,
)


class IntentionalBugTests(unittest.TestCase):
    @unittest.expectedFailure
    def test_binary_search_should_return_the_matching_index(self) -> None:
        self.assertEqual(binary_search_off_by_one([2, 4, 6, 8], 6), 2)

    def test_interpolation_search_bug_exposes_equal_endpoint_case(self) -> None:
        with self.assertRaises(ZeroDivisionError):
            interpolation_search_divide_by_zero([3, 3, 3], 3)

    def test_duplicate_implementations_are_present_for_static_analysis(self) -> None:
        values = [8, 2, 8]
        self.assertEqual(duplicated_linear_scan(values, 8), 0)
        self.assertEqual(duplicated_linear_scan_again(values, 8), 0)


if __name__ == "__main__":
    unittest.main()
