# import pandas as pd
# import matplotlib.pyplot as plt
#
# # Chemin des fichiers CSV
# file_path_feature = "PSK_vector/segmentation/sub_databases/groupe/Feature/courbefiles_feature/FN13_p1.csv"
# file_path_panne = "PSK_vector/segmentation/sub_databases/groupe/Feature/courbefiles_feature/FN13_p1.csv"
#
# # Lire les fichiers CSV
# data_feature = pd.read_csv(file_path_feature)
# data_panne = pd.read_csv(file_path_panne)
#
# # Trier les données en ordre croissant selon les valeurs
# data_feature_sorted = data_feature.sort_values(by="Value")
# data_panne_sorted = data_panne.sort_values(by="Value")
#
# # Extraire les données triées
# x_feature = data_feature_sorted["Value"]
# y_feature = data_feature_sorted["Occurrences"]
#
# x_panne = data_panne_sorted["Value"]
# y_panne = data_panne_sorted["Occurrences"]
#
# # Normaliser les valeurs sur l'axe des Y
# y_feature_normalized = y_feature / y_feature.max()
# y_panne_normalized = y_panne / y_panne.max()
#
# # Déterminer le décalage
# offset = 0.18
#
# # Créer une nouvelle figure
# plt.figure()
#
# # Tracer la courbe de distribution basée sur l'échec
# plt.plot(x_feature, y_feature_normalized, linestyle='-', color='orange', label='Feature distribution based on failure')
#
# # Tracer la courbe de distribution basée sur la fonction avec un décalage
# plt.plot(x_panne, y_panne_normalized + offset, linestyle='-', color='blue', label='Feature distribution based on failure Update')
#
# # Nommer les axes
# plt.xlabel('ΩN13')
# plt.ylabel('Normalized occurrences')
#
# # Ajouter une légende
# plt.legend()
#
# # Afficher la grille
# plt.grid(True)
#
# # Afficher le titre
# plt.title('Calculated based on the reliability factor (FN13)')
#
# # Afficher le graphique
# plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Chemin des fichiers CSV
file_path_feature = "PSK_vector/segmentation/sub_databases/groupe/Feature/courbefiles_feature/FN7_p1.csv"
file_path_panne = "PSK_vector/segmentation/sub_databases/groupe/Feature/courbefiles_feature/FN7_p1.csv"

# Lire les fichiers CSV
data_feature = pd.read_csv(file_path_feature)
data_panne = pd.read_csv(file_path_panne)

# Trier les données en ordre croissant selon les valeurs
data_feature_sorted = data_feature.sort_values(by="Value")
data_panne_sorted = data_panne.sort_values(by="Value")

# Extraire les données triées
x_feature = data_feature_sorted["Value"]
y_feature = data_feature_sorted["Occurrences"]

x_panne = data_panne_sorted["Value"]
y_panne = data_panne_sorted["Occurrences"]

# Normaliser les valeurs sur l'axe des Y
y_feature_normalized = y_feature / y_feature.max()
y_panne_normalized = y_panne / y_panne.max()

# Déterminer la valeur minimale de la courbe normalisée
y_feature_min = y_feature_normalized.min()

# Créer une nouvelle figure
plt.figure()

# Tracer la courbe de distribution basée sur l'échec
plt.plot(x_feature, y_feature_normalized, linestyle='-', color='orange', label='Feature distribution based on failure')

# Tracer une ligne horizontale au point y_min
plt.axhline(y=y_feature_min, color='blue', linestyle='-', label='Feature distribution based on failure Update')

# Nommer les axes
plt.xlabel('ΩN7')
plt.ylabel('Normalized occurrences')

# Ajouter une légende
plt.legend()

# Afficher la grille
plt.grid(True)

# Afficher le titre
plt.title('Calculated based on the reliability factor (FN7)')

# Afficher le graphique
plt.show()
