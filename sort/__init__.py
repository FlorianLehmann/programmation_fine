from sort.insertion import insertion
from sort.fusion import fusion
from sort.heapsort import heap_sort
from sort.quicksort import quick_sort


def python_native_sort_in_place(lst):
	lst.sort()
	return lst


def python_native_not_in_place(lst):
	return sorted(lst)


sorting_algorithms = [
	python_native_sort_in_place,
	python_native_not_in_place,
	insertion,
	fusion,
	heap_sort,
	quick_sort
]

