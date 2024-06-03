import os
import pandas as pd
import matplotlib.pyplot as plt

# Chemin des dossiers contenant les fichiers CSV
feature_folder_path = "PSK_vector/segmentation/sub_databases/groupe/Feature/courbefiles_feature/"
panne_folder_path = "PSK_vector/segmentation/sub_databases/groupe/Panne/courbefiles_pannes/"

# Créer le dossier pour enregistrer les résultats
output_folder_path = "PSK_vector/segmentation/sub_databases/groupe/courbe"
os.makedirs(output_folder_path, exist_ok=True)

# Parcourir tous les fichiers dans le dossier des fonctionnalités
for feature_file in os.listdir(feature_folder_path):
    if feature_file.endswith(".csv"):
        # Lire le fichier CSV
        data_feature = pd.read_csv(os.path.join(feature_folder_path, feature_file))

        # Trier les données en ordre croissant selon les valeurs
        data_feature_sorted = data_feature.sort_values(by="Value")

        # Extraire les données triées
        x_feature = data_feature_sorted["Value"]
        y_feature = data_feature_sorted["Occurrences"]

        # Tracer la courbe
        plt.plot(x_feature, y_feature, marker='o', linestyle='-', label='Cas 1')

# Parcourir tous les fichiers dans le dossier des pannes
for panne_file in os.listdir(panne_folder_path):
    if panne_file.endswith(".csv"):
        # Lire le fichier CSV
        data_panne = pd.read_csv(os.path.join(panne_folder_path, panne_file))

        # Trier les données en ordre croissant selon les valeurs
        data_panne_sorted = data_panne.sort_values(by="value")

        # Extraire les données triées
        x_panne = data_panne_sorted["value"]
        y_panne = data_panne_sorted["occurrences"]

        # Tracer la courbe
        plt.plot(x_panne, y_panne, marker='o', linestyle='-', label='Cas 2')

# Nommer les axes
plt.xlabel('Ω')
plt.ylabel('Occurrences')

# Ajouter une légende
plt.legend()

# Afficher la grille
plt.grid(True)

# Afficher le titre
plt.title('Courbes des Cas 1 et 2')

# Enregistrer le graphique dans le dossier de sortie
output_file_path = os.path.join(output_folder_path, "courbes.png")
plt.savefig(output_file_path)

# Afficher le graphique
plt.show()
