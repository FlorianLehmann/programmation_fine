import time
from sort import *

def experience(generator, max_size_of_array, number_of_iteration = 1000):
    algorithms_runtimes = {}

    # Initialise les listes pour chaque algorithme
    for algorithm in sorting_algorithms:
        algorithms_runtimes[algorithm.__name__] = []

    # Mesure du temps d'exécution moyen pour tous les algorithmes de tris.
    # Cette moyenne est déterminée pour le nombre d'itérations définies dans <number_of_iteration>
    for size in range(max_size_of_array):
        print(size)
        for algorithm in sorting_algorithms:
            tmp_runtimes = []
            for j in range(number_of_iteration):
                start = time.time()
                algorithm(generator(2 ** size))
                stop = time.time()
                tmp_runtimes.append(stop - start)
            mean_runtime = sum(tmp_runtimes) / len(tmp_runtimes)
            algorithms_runtimes[algorithm.__name__].append(mean_runtime)

    return algorithms_runtimes
