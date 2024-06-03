# import pandas as pd
# import matplotlib.pyplot as plt
# import os
# from scipy.interpolate import make_interp_spline
# import numpy as np
#
# # Liste des couleurs pour les courbes
# colors = ['#3b75af', '#add151', '#12223e', 'purple', 'orange', 'brown', 'skyblue', 'darkorange', 'olive', 'cyan']
#
#
# def plot_curve_from_csv(file_path, color):
#     # Lire le fichier CSV
#     data = pd.read_csv(file_path)
#
#     # Trier les valeurs de x dans l'ordre croissant
#     data = data.sort_values(by='Value')
#
#     # Extraire les colonnes "Value" et "Occurrences"
#     x = data["Value"]
#     y = data["Occurrences"]
#
#     # Normaliser les valeurs de y entre 0 et 1
#     y_normalized = y / y.max()
#
#     # Titre basé sur le nom du fichier sans l'extension .csv
#     filename = os.path.basename(file_path)
#     filename_no_extension = os.path.splitext(filename)[0]
#
#     # Extraire failure et feature à partir de filename_no_extension
#     parts = filename_no_extension.split('_')
#     feature = parts[0]
#     failure = parts[1] if len(parts) > 1 else 'unknown'
#
#     # Remplacer fN22 par la variable feature et N22 par la variable feature sans le premier caractère
#     label_feature_removed_first_char = feature[1:] if len(feature) > 1 else feature
#     plot_label = f'$\\pi_1,{label_feature_removed_first_char}$ $(f_{{{label_feature_removed_first_char}}})$'
#
#     # Définir la police Times New Roman
#     font = {'fontname': 'Times New Roman'}
#
#     if feature.startswith("FB"):
#         # Mapper les valeurs de x à "ON" et "OFF"
#         x_labels = ['OFF' if v == 0 else 'ON' for v in x]
#
#         # Tracer le graphique en bâtons pour les features commençant par "FB" avec une largeur réduite
#         plt.bar(x_labels, y_normalized, color=color, width=0.2, label=plot_label)
#         plt.xlabel(f'$\\Omega_{{{label_feature_removed_first_char}}}$', color=color, **font)
#         plt.ylabel('Occurrences (normalized)', color=color, **font)
#         plt.title(f"Normalized average distribution of feature {feature} based on failures ({failure})", **font, color=color)
#     else:
#         if len(x) >= 4:
#             # Créer une interpolation spline
#             x_new = np.linspace(x.min(), x.max(), 300)  # 300 points pour lisser la courbe
#             spline = make_interp_spline(x, y_normalized, k=3)  # k=3 pour une spline cubique
#             y_smooth = spline(x_new)
#         else:
#             # Utiliser l'interpolation linéaire pour moins de 4 points
#             x_new = x
#             y_smooth = y_normalized
#
#         # Tracer la courbe lisse ou linéaire
#         plt.plot(x_new, y_smooth, color=color, linewidth=2, label=plot_label)
#         plt.xlabel(f'$\\Omega_{{{label_feature_removed_first_char}}}$', color=color, **font)
#         plt.ylabel('Occurrences (normalized)', color=color, **font)
#         plt.title(f"Normalized average distribution of feature {feature} based on failures({failure})", **font, color=color)
#
#     # Afficher la grille
#     plt.grid(True)
#
#     # Ajouter la légende
#     plt.legend(prop={'family': 'Times New Roman'})
#
#     # Définir l'échelle de l'axe des Y de 0 à 1.5
#     plt.ylim(0, 1.05)
#
#     # Créer le dossier courbe_feautureBypanne s'il n'existe pas
#     folder_path = os.path.dirname(file_path)
#     save_folder = os.path.join(folder_path, "courbe_feautureBypanne")
#     if not os.path.exists(save_folder):
#         os.makedirs(save_folder)
#
#     # Sauvegarder la figure
#     save_path = os.path.join(save_folder, f"{feature}_{failure}_normalized.png")
#     plt.savefig(save_path)
#
#     # Fermer la figure pour libérer la mémoire
#     plt.close()
#
# # Chemin du dossier contenant les fichiers CSV
# folder_path = "PSK_vector/segmentation/sub_databases/groupe/Feature/courbefiles_feature/"
#
# # Liste des fichiers CSV dans le dossier
# csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
#
# # Dictionnaire pour suivre les couleurs déjà utilisées pour chaque feature
# feature_colors = {}
#
# # Index pour les couleurs
# color_index = 0
#
# # Itérer sur chaque fichier CSV
# for csv_file in csv_files:
#     # Chemin complet du fichier
#     file_path = os.path.join(folder_path, csv_file)
#
#     # Extraire le nom du fichier sans extension pour obtenir le feature
#     filename_no_extension = os.path.splitext(csv_file)[0]
#     feature = filename_no_extension.split('_')[0]
#
#     # Assigner une couleur à chaque feature
#     if feature not in feature_colors:
#         feature_colors[feature] = colors[color_index % len(colors)]
#         color_index += 1
#
#     # Appeler la fonction plot_curve_from_csv pour tracer la courbe et sauvegarder la figure
#     plot_curve_from_csv(file_path, feature_colors[feature])

