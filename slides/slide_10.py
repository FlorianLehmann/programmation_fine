import csv
import matplotlib.pyplot as plt


def main():
    plt.switch_backend('Qt5Agg')

    fig, ax = plt.subplots()
    ax.grid(True, alpha=0.3)

    with open("slide_10.csv") as csv_file:
        reader = csv.DictReader(csv_file)
        x = list(map(int, reader.fieldnames[1:]))
        for row in reader:
            y = [float(row[str(e)]) for e in x]
            ax.plot(x, y, label=row["data"])

    ax.set_xlabel("taille pour appliqué le tri par insertion")
    ax.set_ylabel("temps d'execution en secondes")
    ax.set_title('Comparaison des valeurs de seuils pour le tri rapide', size=20)
    ax.legend()
    plt.show()


if __name__ == '__main__':
    main()