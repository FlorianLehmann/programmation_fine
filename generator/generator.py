import random


def constant_array(n, value=None):
    if value is None:
        value = random.randrange(1000)
    return [value for _ in range(n)]


def random_array(n, max_value=1000):
    return [random.randrange(max_value) for _ in range(n)]


def sorted_array(n, max_value=1000):
    return sorted(random_array(n, max_value))


def reverse_sorted_array(n, max_value=1000):
    return reversed(sorted_array(n, max_value))

