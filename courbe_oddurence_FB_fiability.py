import pandas as pd
import matplotlib.pyplot as plt
import os


def excel_to_csv(excel_file, sheet_name, csv_file):
    # Lire le fichier Excel
    df = pd.read_excel(excel_file, sheet_name=sheet_name)
    # Convertir en fichier CSV
    df.to_csv(csv_file, index=False)


def create_bar_charts(csv_file, output_dir):
    # Lire le fichier CSV
    df = pd.read_csv(csv_file)

    # Extraire les colonnes nécessaires
    columns = df.columns[
              1:]  # Supposons que la première colonne soit l'index ou une autre colonne non nécessaire pour les barres

    # Créer des couleurs uniques pour chaque colonne
    colors = plt.cm.get_cmap('tab10', len(columns)).colors

    # Créer un répertoire pour enregistrer les figures
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Créer une figure pour chaque ligne
    for i, row in df.iterrows():
        plt.figure()
        x_labels = [f'c{j + 1}' for j in range(len(columns))]
        y_values = row[columns].values

        plt.bar(x_labels, y_values, color=colors)
        plt.xlabel('Colonnes')
        plt.ylabel('Occurrences')
        plt.title(f'Figure pour la ligne {i + 1}')
        plt.legend(columns, title='Légende')

        # Enregistrer la figure
        plt.savefig(os.path.join(output_dir, f'figure_{i + 1}.png'))
        plt.close()


# Exemple d'utilisation
excel_file = 'sourceFiles/nboccurence_bar.xlsx'  # Remplacer par le nom de votre fichier Excel
sheet_name = 'Sheet1'  # Remplacer par le nom de votre feuille
csv_file = 'sourceFiles/nboccurence_bar.csv'
output_dir = 'courbe'

# Convertir l'Excel en CSV
excel_to_csv(excel_file, sheet_name, csv_file)

# Créer des graphiques en barres
create_bar_charts(csv_file, output_dir)
