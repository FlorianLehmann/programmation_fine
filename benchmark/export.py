import csv
import os

def export_to_csv(result, filename):
    dir = os.path.dirname(filename)
    if not os.path.exists(dir):
        os.mkdir(dir)
    with open(filename, "w") as csv_file:
        writer = csv.writer(csv_file)
        for key, value in result.items():
            writer.writerow([key, value])