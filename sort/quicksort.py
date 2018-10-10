import random


def always_low_value(lst, low, high):
    return low


def always_mid_element(lst, low, high):
    return (high + low) // 2


def always_high_value(lst, low, high):
    return high


def random_pivot(lst, low, high):
    return random.randrange(low, high + 1)


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
    if lst[mid] > lst[high]:
        return high
    return mid


def find_pivot_by_median_of_5_values(lst, low, high):
    q1, mid, q3 = low + (high - low) // 4, low + (high - low) // 2, low + (high - low) * 3 // 4
    if lst[low] < lst[q1]:
        if lst[q1] < lst[mid]:
            if lst[q3] < lst[high]:
                if lst[high] < lst[mid]:
                    if lst[high] > lst[q1]:
                        if lst[q3] > lst[q1]:
                            return q3
                        return q1
                    if lst[high] > lst[low]:
                        return high
                    return low
                if lst[mid] < lst[q3]:
                    return mid
                if lst[q3] > lst[q1]:
                    return q3
                return q1
            if lst[q3] < lst[mid]:
                if lst[q3] > lst[q1]:
                    if lst[high] > lst[q1]:
                        return high
                    return q1
                if lst[q3] > lst[low]:
                    return q3
                return low
            if lst[mid] < lst[high]:
                return mid
            if lst[high] > lst[q1]:
                return high
            return q1
        if lst[mid] > lst[low]:
            if lst[q3] < lst[high]:
                if lst[high] < lst[q1]:
                    if lst[high] > lst[mid]:
                        if lst[q3] > lst[mid]:
                            return q3
                        return mid
                    if lst[high] > lst[low]:
                        return high
                    return low
                if lst[q1] < lst[q3]:
                    return q1
                if lst[q3] > lst[mid]:
                    return q3
                return mid
            if lst[q3] < lst[q1]:
                if lst[q3] > lst[mid]:
                    if lst[high] > lst[mid]:
                        return high
                    return mid
                if lst[q3] > lst[low]:
                    return q3
                return low
            if lst[q1] < lst[high]:
                return q1
            if lst[high] > lst[mid]:
                return high
            return mid
        if lst[q3] < lst[high]:
            if lst[high] < lst[q1]:
                if lst[high] > lst[low]:
                    if lst[q3] > lst[low]:
                        return q3
                    return low
                if lst[high] > lst[mid]:
                    return high
                return mid
            if lst[q1] < lst[q3]:
                return q1
            if lst[q3] > lst[low]:
                return q3
            return low
        if lst[q3] < lst[q1]:
            if lst[q3] > lst[low]:
                if lst[high] > lst[low]:
                    return high
                return low
            if lst[q3] > lst[mid]:
                return q3
            return mid
        if lst[q1] < lst[high]:
            return q1
        if lst[high] > lst[low]:
            return high
        return low
    if lst[low] < lst[mid]:
        if lst[q3] < lst[high]:
            if lst[high] < lst[mid]:
                if lst[high] > lst[low]:
                    if lst[q3] > lst[low]:
                        return q3
                    return low
                if lst[high] > lst[q1]:
                    return high
                return q1
            if lst[mid] < lst[q3]:
                return mid
            if lst[q3] > lst[low]:
                return q3
            return low
        if lst[q3] < lst[mid]:
            if lst[q3] > lst[low]:
                if lst[high] > lst[low]:
                    return high
                return low
            if lst[q3] > lst[q1]:
                return q3
            return q1
        if lst[mid] < lst[high]:
            return mid
        if lst[high] > lst[low]:
            return high
        return low
    if lst[mid] > lst[q1]:
        if lst[q3] < lst[high]:
            if lst[high] < lst[low]:
                if lst[high] > lst[mid]:
                    if lst[q3] > lst[mid]:
                        return q3
                    return mid
                if lst[high] > lst[q1]:
                    return high
                return q1
            if lst[low] < lst[q3]:
                return low
            if lst[q3] > lst[mid]:
                return q3
            return mid
        if lst[q3] < lst[low]:
            if lst[q3] > lst[mid]:
                if lst[high] > lst[mid]:
                    return high
                return mid
            if lst[q3] > lst[q1]:
                return q3
            return q1
        if lst[low] < lst[high]:
            return low
        if lst[high] > lst[mid]:
            return high
        return mid
    if lst[q3] < lst[high]:
        if lst[high] < lst[low]:
            if lst[high] > lst[q1]:
                if lst[q3] > lst[q1]:
                    return q3
                return q1
            if lst[high] > lst[mid]:
                return high
            return mid
        if lst[low] < lst[q3]:
            return low
        if lst[q3] > lst[q1]:
            return q3
        return q1
    if lst[q3] < lst[low]:
        if lst[q3] > lst[q1]:
            if lst[high] > lst[q1]:
                return high
            return q1
        if lst[q3] > lst[mid]:
            return q3
        return mid
    if lst[low] < lst[high]:
        return low
    if lst[high] > lst[q1]:
        return high
    return q1


pivot_functions = [
    always_low_value,
    always_mid_element,
    always_high_value,
    random_pivot,
    find_pivot_by_median_of_3_values,
    find_pivot_by_median_of_5_values
]


def partition(lst, low, high, pivot):
    lst[high], lst[pivot] = lst[pivot], lst[high]
    pivot_value = lst[high]
    pointer = low
    for i in range(low, high):
        if (i <= pivot and lst[i] <= pivot_value) or (i > pivot and lst[i] < pivot_value):
            if i != pointer:
                lst[i], lst[pointer] = lst[pointer], lst[i]
            pointer += 1
    lst[pointer], lst[high] = lst[high], lst[pointer]
    return pointer


def quick_sort(lst, low=0, high=None, min_size=10, pivot_function=find_pivot_by_median_of_3_values):
    if high is None:
        high = len(lst) - 1
    if (high - low) < min_size:
        return insertion(lst, low, high)
    if low < high:
        pivot = pivot_function(lst, low, high)
        pivot = partition(lst, low, high, pivot)
        quick_sort(lst, low, pivot - 1, min_size, pivot_function)
        quick_sort(lst, pivot + 1, high, min_size, pivot_function)
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
