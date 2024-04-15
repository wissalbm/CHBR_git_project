import pandas as pd
import matplotlib.pyplot as plt

# Chemin des fichiers CSV
file_path_feature = "PSK_vector/segmentation/sub_databases/groupe/Feature/courbefiles_feature/FB1_p1.csv"
file_path_panne = "PSK_vector/segmentation/sub_databases/groupe/Panne/courbefiles_pannes/p1_FB1_Value.csv"

# Lire les fichiers CSV
data_feature = pd.read_csv(file_path_feature)
data_panne = pd.read_csv(file_path_panne)

# Extraire les données des fichiers
x_feature = data_feature["Value"]
y_feature = data_feature["Occurrences"]

x_panne = data_panne["value"]
y_panne = data_panne["occurrences"]

# Tracer les courbes
plt.plot(x_feature, y_feature, marker='o', linestyle='-', color='orange', label='Cas 1')
plt.plot(x_panne, y_panne, marker='o', linestyle='-', color='purple', label='Cas 2')

# Nommer les axes
plt.xlabel('Ω')
plt.ylabel('Occurrences')

# Ajouter une légende
plt.legend()

# Afficher la grille
plt.grid(True)

# Afficher le titre
plt.title('Courbes des Cas 1 et 2')

# Afficher le graphique
plt.show()
