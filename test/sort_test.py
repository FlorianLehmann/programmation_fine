import unittest

from generator import *
from sort import *
from sort.quicksort import pivot_functions, quick_sort


class SortTest(unittest.TestCase):

    def test_should_sort_reverse_array(self):
        numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for algorithm in sorting_algorithms:
            actual = algorithm(list(numbers))
            self.assertEqual(expected, actual)

    def test_should_sort_reverse_array_2(self):
        numbers = reverse_sorted_array(2**10)
        expected = sorted(numbers)
        for algorithm in sorting_algorithms:
            actual = algorithm(list(numbers))
            self.assertEqual(expected, actual)

    def test_should_sort_sorted_array(self):
        numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for algorithm in sorting_algorithms:
            actual = algorithm(list(numbers))
            self.assertEqual(expected, actual)

    def test_should_sort_sorted_array_2(self):
        numbers = sorted_array(2**10)
        expected = sorted(numbers)
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

    def test_should_sort_random_array_2(self):
        numbers = random_array(2**10)
        expected = sorted(numbers)
        for algorithm in sorting_algorithms:
            actual = algorithm(list(numbers))
            self.assertEqual(expected, actual)

    def test_pivot(self):
        numbers = random_array(2**10)
        expected = sorted(numbers)
        for pivot in pivot_functions:
            actual = quick_sort(list(numbers), pivot_function=pivot)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
