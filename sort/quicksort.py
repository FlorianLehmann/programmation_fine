
def naive_pivot(lst, low, high):
    return low


def find_pivot_by_median_of_3_values(lst, low, high):
    mid = low + (high - low) // 2
    if lst[mid] < lst[low]:
        if lst[low] < lst[high]:
            return low
        if lst[mid] > lst[high]:
            return mid
        return high
    if lst[low] > lst[high]:
        return low
    if lst[mid] < lst[high]:
        return mid
    return high


pivot_functions = [
    naive_pivot,
    find_pivot_by_median_of_3_values,
]


def partition(lst, low, high, pivot):
    pointer = low
    pivot_value = lst[pivot]
    for i in range(low, high):
        if lst[i] < pivot_value:
            if pointer != i:
                lst[pointer], lst[i] = lst[i], lst[pointer]
            pointer += 1
    return pointer


def quick_sort(lst, low=0, high=None, min_size=10, pivot_function=find_pivot_by_median_of_3_values):
    if high is None:
        high = len(lst) - 1
    if (high - low) < min_size:
        return insertion(lst, low, high)
    pivot = pivot_function(lst, low, high)
    pivot = partition(lst, low, high, pivot)
    quick_sort(lst, low, pivot - 1)
    quick_sort(lst, pivot + 1, high)
    return lst


def insertion(numbers, start, end):
    for i in range(start + 1, end + 1):
        tmp = i
        for j in reversed(range(start, i)):
            if numbers[tmp] >= numbers[j]:
                break
            else:
                numbers[tmp], numbers[j] = numbers[j], numbers[tmp]
                tmp = tmp - 1
    return numbers
