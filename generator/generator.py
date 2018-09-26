import random


def random_array(n, max_value=1000):
    return [random.randrange(max_value) for _ in range(n)]

