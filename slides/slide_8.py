from collections import defaultdict
import glob
import csv
from math import log
import os

import numpy as np


def coefficient(x, y):
    return np.cov(x, y)[0][1] / np.var(x)


def main():
    algorithms = set()
    output = defaultdict(lambda: defaultdict(float))

    for filename in glob.glob("../output/*.csv"):
        with open(filename) as csv_file:
            reader = csv.reader(csv_file)
            results = dict(reader)

        for key, value in results.items():
            algorithms.add(key)
            results[key] = eval(value)

        for key, value in results.items():
            results[key] = [log(e, 10) for e in value]

        for key, value in results.items():
            x = np.linspace(0, len(value), len(value))
            output[filename][key] = round(coefficient(x[7:], value[7:]), 3)

    with open("slide_8.csv", "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["data"] + list(algorithms))
        writer.writeheader()
        for filename, values in output.items():
            writer.writerow({"data": os.path.splitext(os.path.basename(filename))[0], **values})


if __name__ == '__main__':
    main()
