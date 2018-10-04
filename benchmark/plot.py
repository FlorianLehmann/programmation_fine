import csv
from math import log
import numpy as np
import matplotlib.pyplot as plt

def main():
	with open('results.csv', 'r') as csv_file:
		reader = csv.reader(csv_file)
		results = dict(reader)
	for key, value in results.items():
		results[key] = eval(value)

	for key, value in results.items():
		results[key] = [log(e, 10) for e in value]

	for key, value in results.items():
		x = np.linspace(0, len(value), len(value))
		plt.plot(x, value, label=key)

	plt.xlabel("number of elements (log 2)")
	plt.ylabel("seconds of execution (log 10)")
	plt.legend()
	plt.show()


if __name__ == '__main__':
	main()
