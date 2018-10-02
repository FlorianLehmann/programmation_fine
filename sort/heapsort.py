def parent(i):
	return (i - 1) // 2


def left_child(i):
	return 2 * i + 1


def right_child(i):
	return 2 * i + 2


def heapify(lst):
	start = parent(len(lst) - 1)
	while start >= 0:
		sift_down(lst, start, len(lst) - 1)
		start -= 1


def sift_down(lst, start, end):
	root = start
	while left_child(root) <= end:
		child = left_child(root)
		swap = root
		if lst[swap] < lst[child]:
			swap = child
		if child + 1 <= end and lst[swap] < lst[child + 1]:
			swap = child + 1
		if swap == root:
			return
		else:
			lst[root], lst[swap] = lst[swap], lst[root]
			root = swap


def heap_sort(lst):
	heapify(lst)
	end = len(lst) - 1
	while end > 0:
		lst[0], lst[end] = lst[end], lst[0]
		end -= 1
		sift_down(lst, 0, end)
	return lst
