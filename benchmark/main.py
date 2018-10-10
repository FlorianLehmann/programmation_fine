from collections import defaultdict
import csv
import os
from statistics import mean
from time import time

from benchmark.export import export_to_csv
from benchmark.experience import experience
from benchmark.timeout import Timeout
from generator import *
from sort.quicksort import pivot_functions, quick_sort
import platform


implementation = platform.python_implementation()

output_folder = "output" if implementation == "PyPy" else "output_sans_pypy"


def bench_sorting_algorithms():
    for generator in generator_algorithms:
        result = experience(generator, 30)
        export_to_csv(result, os.path.join("..", output_folder, generator.__name__ + ".csv"))


def bench_quicksort_pivot_functions():
    result = defaultdict(lambda: defaultdict())
    for generator in generator_algorithms:
        print(generator.__name__)
        for pivot_function in pivot_functions:
            print(pivot_function.__name__)
            temp = []
            try:
                with Timeout(3):
                    for _ in range(1000):
                        start = time()
                        quick_sort(generator(2 ** 14), pivot_function=pivot_function)
                        temp.append(time() - start)
            except Exception as e:
                print("Oups", e)
            if temp:
                result[generator.__name__][pivot_function.__name__] = round(mean(temp), 5)
            else:
                print("No values for", pivot_function.__name__)

    filename = os.path.join("..", "slides", "slide_9.csv")
    dir = os.path.dirname(filename)
    if not os.path.exists(dir):
        os.mkdir(dir)
    with open(filename, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["data"] + [pivot.__name__ for pivot in pivot_functions])
        writer.writeheader()
        for key, value in result.items():
            writer.writerow({"data": key, **value})


def bench_quicksort_insertion_size():
    result = defaultdict(lambda: defaultdict())
    sizes = list(range(1, 200, 10))
    for generator in generator_algorithms:
        print(generator.__name__)
        for size in sizes:
            print(size)
            temp = []
            try:
                with Timeout(1):
                    for _ in range(100):
                        start = time()
                        quick_sort(generator(2 ** 14), min_size=size)
                        temp.append(time() - start)
            except Exception as e:
                print("Oups", e)
            if temp:
                result[generator.__name__][size] = round(mean(temp), 5)
            else:
                print("No values for", size)

    filename = os.path.join("..", "slides", "slide_10.csv")
    dir = os.path.dirname(filename)
    if not os.path.exists(dir):
        os.mkdir(dir)
    with open(filename, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["data"] + sizes)
        writer.writeheader()
        for key, value in result.items():
            writer.writerow({"data": key, **value})


def main():
    # bench_sorting_algorithms()
    # bench_quicksort_pivot_functions()
    bench_quicksort_insertion_size()

if __name__ == '__main__':
    main()
