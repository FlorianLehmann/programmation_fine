from statistics import mean
import time
from sort import *
from benchmark.timeout import Timeout


def experience(generator, max_size_of_array, number_of_iteration=1000):
    algorithms_runtimes = {}
    algorithms = list(sorting_algorithms)
    # Initialise les listes pour chaque algorithme
    for algorithm in algorithms:
        algorithms_runtimes[algorithm.__name__] = []

    # Mesure du temps d'exécution moyen pour tous les algorithmes de tris.
    # Cette moyenne est déterminée pour le nombre d'itérations définies dans <number_of_iteration>
    for size in range(max_size_of_array):
        print(size)
        to_remove = []
        for algorithm in algorithms:
            tmp_runtimes = []
            try:
                with Timeout(10):
                    for j in range(number_of_iteration):
                        start = time.time()
                        try:
                            algorithm(generator(2 ** size))
                        except RuntimeError as e:
                            print("Oups, something went wrong for", algorithm.__name__, ":", e)
                        stop = time.time()
                        tmp_runtimes.append(stop - start)
            except Timeout.Timeout:
                print("Stop ", algorithm.__name__, "after ", len(tmp_runtimes), "iterations")
                if len(tmp_runtimes) <= 100:
                    # Not enough instances to compute a correct mean
                    to_remove.append(algorithm)
                    print("Removes ", algorithm.__name__, "from the running algorithms")
            if tmp_runtimes:
                algorithms_runtimes[algorithm.__name__].append(mean(tmp_runtimes))
        for algorithm in to_remove:
            algorithms.remove(algorithm)

    return algorithms_runtimes
