import time
from sort import *
import csv
import signal


class Timeout():
    """Timeout class using ALARM signal."""

    class Timeout(Exception):
        pass

    def __init__(self, sec):
        self.sec = sec

    def __enter__(self):
        signal.signal(signal.SIGALRM, self.raise_timeout)
        signal.alarm(self.sec)

    def __exit__(self, *args):
        signal.alarm(0)  # disable alarm

    def raise_timeout(self, *args):
        raise Timeout.Timeout()


def experience(generator, max_size_of_array, number_of_iteration = 1000):
    algorithms_runtimes = {}

    # Initialise les listes pour chaque algorithme
    for algorithm in sorting_algorithms:
        algorithms_runtimes[algorithm.__name__] = []

    # Mesure du temps d'exécution moyen pour tous les algorithmes de tris.
    # Cette moyenne est déterminée pour le nombre d'itérations définies dans <number_of_iteration>
    for size in range(max_size_of_array):
        print(size)
        to_remove = []
        for algorithm in sorting_algorithms:
            tmp_runtimes = []
            try:
                with Timeout(10):
                    for j in range(number_of_iteration):
                        start = time.time()
                        algorithm(generator(2 ** size))
                        stop = time.time()
                        tmp_runtimes.append(stop - start)
            except Timeout.Timeout:
                print("Stop ", algorithm.__name__, "after ", len(tmp_runtimes), "iterations")
                if j <= 100:
                    # Not enough instances to compute a correct mean
                    to_remove.append(algorithm)
                    print("Removes ", algorithm.__name__, "from the running algorithms")
            mean_runtime = None if not len(tmp_runtimes) else sum(tmp_runtimes) / len(tmp_runtimes)
            if mean_runtime is not None:
                algorithms_runtimes[algorithm.__name__].append(mean_runtime)
        for algorithm in to_remove:
            sorting_algorithms.remove(algorithm)

    return algorithms_runtimes


def export_to_csv(result):
    with open("results.csv", "w") as csv_file:
        writer = csv.writer(csv_file)
        for key, value in result.items():
            writer.writerow([key, value])


if __name__ == "__main__":
    from generator import random_array
    export_to_csv(experience(random_array, 28))
