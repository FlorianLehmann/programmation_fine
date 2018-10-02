from . import insertion


def find_pivot(lst, low, high):
	return lst[high]


def find_pivot_by_median_of_3_values(lst, low, high):
	mid = (low + high) // 2
	if lst[mid] < lst[low]:
		lst[low], lst[mid] = lst[mid], lst[low]
	if lst[high] < lst[low]:
		lst[low], lst[high] = lst[high], lst[low]
	if lst[mid] < lst[high]:
		lst[low], lst[high] = lst[high], lst[low]
	return lst[high]


def find_pivot_by_median_of_5_values(lst, low, high):
	quartiles = [low + (high - low) * i // 4 for i in range(5)]
	for i, x in enumerate(quartiles):
		for j, y in enumerate(quartiles[i:], i):
			if lst[y] < lst[x]:
				lst[x], lst[y] = lst[y], lst[x]
	return lst[high]


def find_pivot_by_median_of_2_times_n_plus_1_values(lst, low, high, n=3):
	m = 2 * n + 1
	quartiles = [low + (high - low) * i // (m - 1) for i in range(m)]
	for i, x in enumerate(quartiles):
		for j, y in enumerate(quartiles[i:], i):
			if lst[y] < lst[x]:
				lst[x], lst[y] = lst[y], lst[x]
	return lst[high]


pivot_functions = [
	find_pivot,
	find_pivot_by_median_of_3_values,
	find_pivot_by_median_of_5_values,
	find_pivot_by_median_of_2_times_n_plus_1_values
]


def partition(lst, low, high, pivot):
	i = low
	for j in range(low, high):
		if lst[j] < pivot:
			lst[i], lst[j] = lst[j], lst[i]
			i += 1
	lst[i], lst[high] = lst[high], lst[i]
	return i


def quick_sort(lst, low=0, high=None, min_size=10, pivot_function=find_pivot_by_median_of_3_values):
	if high is None:
		high = len(lst) - 1
	if len(lst) < min_size:
		return insertion(lst)
	if low < high:
		p = pivot_function(lst, low, high)
		partition(lst, low, high, p)
		quick_sort(lst, low, p - 1)
		quick_sort(lst, p + 1, high)
	return lst
