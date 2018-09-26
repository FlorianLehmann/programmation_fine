import unittest
from sort import *


class SortTest(unittest.TestCase):

    def test_should_sort_reverse_array(self):
        numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for algorithm in sorting_algorithms:
            actual = algorithm(list(numbers))
            self.assertEqual(expected, actual)

    def test_should_sort_sorted_array(self):
        numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for algorithm in sorting_algorithms:
            actual = algorithm(list(numbers))
            self.assertEqual(expected, actual)

    def test_should_sort_empty_array(self):
        numbers = []
        expected = []
        for algorithm in sorting_algorithms:
            actual = algorithm(list(numbers))
            self.assertEqual(expected, actual)

    def test_should_sort_random_array(self):
        numbers = [3, 4, 0, 1, 13, 7]
        expected = [0, 1, 3, 4, 7, 13]
        for algorithm in sorting_algorithms:
            actual = algorithm(list(numbers))
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
