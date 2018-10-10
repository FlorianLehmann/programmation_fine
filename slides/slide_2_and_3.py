import csv

import numpy as np
from math import log
import matplotlib.pyplot as plt
from mpld3 import plugins


def coefficient(x, y):
    return np.cov(x, y)[0][1] / np.var(x)


def main():
    plt.switch_backend('Qt5Agg')

    fig, ax = plt.subplots()
    ax.grid(True, alpha=0.3)


    with open("../output/random_array.csv") as csv_file:
        reader = csv.reader(csv_file)
        results = dict(reader)

    for key, value in results.items():
        results[key] = eval(value)

    for key, value in results.items():
        results[key] = [log(e, 10) for e in value]

    for key, value in results.items():
        x = np.linspace(0, len(value), len(value))
        ax.plot(x, value, label=f"{key}")
        ax.get_legend_handles_labels()

    handles, labels = ax.get_legend_handles_labels()  # return lines and labels
    interactive_legend = plugins.InteractiveLegendPlugin(zip(handles,
                                                             ax.collections),
                                                         labels,
                                                         alpha_unsel=0.5,
                                                         alpha_over=1.5,
                                                         start_visible=True)
    plugins.connect(fig, interactive_legend)

    ax.set_xlabel("nombre d'éléments (log 2)")
    ax.set_ylabel("temps d'execution en secondes (log 10)")
    ax.set_title('Exécution des algorithmes sur\nune liste générée aléatoirement', size=20)
    ax.legend()
    plt.show()


if __name__ == '__main__':
    main()
