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


def partition(lst, low, high):
	pivot = find_pivot_by_median_of_3_values(lst, low, high)
	i = low
	for j in range(low, high):
		if lst[j] < pivot:
			lst[i], lst[j] = lst[j], lst[i]
			i += 1
	lst[i], lst[high] = lst[high], lst[i]
	return i


def quick_sort(lst, low=0, high=None):
	if high is None:
		high = len(lst) - 1
	if low < high:
		p = partition(lst, low, high)
		quick_sort(lst, low, p - 1)
		quick_sort(lst, p + 1, high)
	return lst
