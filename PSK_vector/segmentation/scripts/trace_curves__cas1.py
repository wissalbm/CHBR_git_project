import pandas as pd
import matplotlib.pyplot as plt
import os

def plot_curve_from_csv(file_path):

    # Lire le fichier CSV
    data = pd.read_csv(file_path)

    # Trier les valeurs de x dans l'ordre croissant
    data = data.sort_values(by='Value')

    # Extraire les colonnes "Value" et "Occurrences"
    x = data["Value"]
    y = data["Occurrences"]

    # Tracer la courbe
    plt.plot(x, y, marker='o', linestyle='-', color='orange')

    # Nommer les axes
    plt.xlabel('Ω')
    plt.ylabel('Occurrences')

    # Titre basé sur le nom du fichier sans l'extension .csv
    filename = os.path.basename(file_path)
    filename_no_extension = os.path.splitext(filename)[0]
    plt.title(f"{filename_no_extension}")

    # Afficher la grille
    plt.grid(True)

    # Créer le dossier courbe_feautureBypanne s'il n'existe pas
    folder_path = os.path.dirname(file_path)
    save_folder = os.path.join(folder_path, "courbe_feautureBypanne")
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    # Sauvegarder la figure
    save_path = os.path.join(save_folder, f"{filename_no_extension}.png")
    plt.savefig(save_path)

    # Fermer la figure pour libérer la mémoire
    plt.close()

# Chemin du dossier contenant les fichiers CSV
folder_path = "PSK_vector/segmentation/sub_databases/groupe/Feature/courbefiles_feature/"

# Liste des fichiers CSV dans le dossier
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

# Itérer sur chaque fichier CSV
for csv_file in csv_files:
    # Chemin complet du fichier
    file_path = os.path.join(folder_path, csv_file)
    # Appeler la fonction plot_curve_from_csv pour tracer la courbe et sauvegarder la figure
    plot_curve_from_csv(file_path)
