import random
import sys
import math


MAX_INT = sys.maxsize


def constant_array(n, value=None):
    if value is None:
        value = random.randrange(MAX_INT)
    return [value for _ in range(n)]


def random_array(n, max_value=MAX_INT):
    return [random.randrange(max_value) for _ in range(n)]


def random_log_array(n, max_value=MAX_INT):
    return random_array(n, int(math.log(max_value)))


def random_squared_array(n, max_value=MAX_INT):
    return random_array(n, max_value ** 2)


def sorted_array(n, max_value=MAX_INT):
    return sorted(random_array(n, max_value))


def reverse_sorted_array(n, max_value=MAX_INT):
    return reversed(sorted_array(n, max_value))

