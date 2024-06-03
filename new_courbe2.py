import random
import csv
import matplotlib.pyplot as plt
from collections import Counter
import os
import pandas as pd


def plot_csv_data(file_path, output_dir):
    # Lecture du fichier CSV avec pandas
    df = pd.read_csv(file_path)

    # Créer un répertoire de sortie s'il n'existe pas
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Itérer sur chaque colonne
    for column_name in df.columns:
        # Sauvegarder la courbe pour chaque colonne
        plot_title = f"Primitive '{column_name}'"
        plot_csv_data_single_column(df[column_name], plot_title, output_dir, f"courbe_primitive_{column_name}.png", column_name)

def plot_csv_data_single_column(column_data, plot_title, output_dir, filename, label):
    # Extraction des différentes valeurs et comptage de leurs occurrences
    value_counter = Counter(column_data)
    # Tri des paires (valeur, occurrence) en fonction des valeurs
    sorted_pairs = sorted(value_counter.items(), key=lambda x: x[0])

    # Récupération des valeurs et des occurrences triées
    values, occurrences = zip(*sorted_pairs)

    # Tracé de la courbe
    plt.plot(values, occurrences, marker='o', linestyle='-', color='orange', linewidth=2, label=label)  # Élargissement de la courbe
    plt.xlabel('Ω (Omega)')  # Ajout de l'étiquette pour l'axe x
    plt.ylabel("Number of occurrences (Frequency)")  # Ajout de l'étiquette pour l'axe y
    plt.title(plot_title)
    plt.grid(True)  # Ajout de la grille
    plt.legend()  # Ajout de l'étiquette

    # Ajustement de l'échelle de l'axe des ordonnées
    max_occurrence = max(occurrences)
    plt.ylim(0, max_occurrence + max_occurrence * 0.1)  # Ajustement de l'échelle pour inclure toutes les valeurs d'occurrence

    # Sauvegarder le graphique dans un fichier
    plt.savefig(os.path.join(output_dir, filename))
    plt.close()

plot_csv_data("pretreatment/files/vecteurcsv_withEntete.csv", "courbe_result_good2")
