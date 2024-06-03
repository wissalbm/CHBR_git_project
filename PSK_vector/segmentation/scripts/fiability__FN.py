import pandas as pd
import matplotlib.pyplot as plt
import os
from scipy.interpolate import make_interp_spline
import numpy as np

# Liste des couleurs pour les courbes
colors = ['blue', '#52b5da']  # #12223e (bleu foncé) et #52b5da (bleu ciel)


def plot_curve_from_csv(file_path, color, label, offset=0, linestyle='-'):
    # Lire le fichier CSV
    data = pd.read_csv(file_path)

    # Trier les valeurs de x dans l'ordre croissant
    data = data.sort_values(by='Value')

    # Extraire les colonnes "Value" et "Occurrences"
    x = data["Value"]
    y = data["Occurrences"]

    # Normaliser les valeurs de y entre 0 et 1
    y_normalized = y / y.max()

    # Extraire feature et failure à partir du nom du fichier sans l'extension .csv
    filename_no_extension = os.path.splitext(os.path.basename(file_path))[0]
    parts = filename_no_extension.split('_')
    feature = parts[0]
    failure = parts[1] if len(parts) > 1 else 'unknown'

    # Définir la police Times New Roman
    font = {'fontname': 'Times New Roman'}

    # Remplacer fN22 par la variable feature et N22 par la variable feature sans le premier caractère
    label_feature_removed_first_char = feature[1:] if len(feature) > 1 else feature

    if feature.startswith("FB"):
        # Mapper les valeurs de x à "ON" et "OFF"
        x_labels = ['OFF' if v == 0 else 'ON' for v in x]

        # Tracer le graphique en bâtons pour les features commençant par "FB" avec une largeur réduite
        plt.bar(x_labels, y_normalized + offset, color=color, width=0.2, label=label)
        plt.xlabel(f'Ω{label_feature_removed_first_char}', color='blue', **font)
        plt.ylabel('Occurrences (normalized)', color='blue', **font)
        plt.title(f"Updating possibility distribution using the reliability factor {feature}_{failure}", **font,
                  color='blue')
    else:
        if len(x) >= 4:
            # Créer une interpolation spline
            x_new = np.linspace(x.min(), x.max(), 300)  # 300 points pour lisser la courbe
            spline = make_interp_spline(x, y_normalized, k=3)  # k=3 pour une spline cubique
            y_smooth = spline(x_new)
        else:
            # Utiliser l'interpolation linéaire pour moins de 4 points
            x_new = x
            y_smooth = y_normalized

        if filename_no_extension == "FN7_p1" and color == '#52b5da':
            # Tracer une ligne horizontale à y=0.70 pour FN7_p1 en bleu ciel
            y_fixed = 0.70
            plt.plot(x_new, [y_fixed + offset] * len(x_new), color=color, linewidth=2, linestyle=linestyle, label=label)
        else:
            # Tracer la courbe lisse ou linéaire
            plt.plot(x_new, y_smooth + offset, color=color, linewidth=2, linestyle=linestyle, label=label)

        plt.xlabel(f'Ω{label_feature_removed_first_char}', color='blue', **font)
        plt.ylabel('Occurrences (normalized)', color='blue', **font)
        plt.title(f"Updating possibility distribution using the reliability factor {feature}_{failure}", **font,
                  color='blue')

    # Afficher la grille
    plt.grid(True)


# Fonction pour tracer et sauvegarder la figure
def plot_and_save(file_path, offsets, labels, linestyles, filename):
    for color, label, offset, linestyle in zip(colors, labels, offsets, linestyles):
        plot_curve_from_csv(file_path, color, label, offset, linestyle)

    # Ajouter la légende
    plt.legend(prop={'family': 'Times New Roman'})

    # Sauvegarder la figure dans le dossier approprié
    save_folder = os.path.join(os.path.dirname(file_path), "courbe_feautureBypanne")
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    save_path = os.path.join(save_folder, filename)
    plt.savefig(save_path)

    # Afficher la figure
    plt.show()

# Chemins des fichiers CSV
file_path_FN22 = "PSK_vector/segmentation/sub_databases/groupe/Feature/courbefiles_feature/FN22_p1.csv"
file_path_FN14 = "PSK_vector/segmentation/sub_databases/groupe/Feature/courbefiles_feature/FN14_p1.csv"
file_path_FN13 = "PSK_vector/segmentation/sub_databases/groupe/Feature/courbefiles_feature/FN13_p1.csv"
file_path_FN7 = "PSK_vector/segmentation/sub_databases/groupe/Feature/courbefiles_feature/FN7_p1.csv"

# Tracer et sauvegarder la figure pour FN22_p1
plot_and_save(file_path_FN22, [0, 0.03],
              ['Possibility distributions', 'Updated possibility distributions using the reliability factor'],
              ['-', '--'], "FN22_p1_normalized.png")

# Tracer et sauvegarder la figure pour FN14_p1
plot_and_save(file_path_FN14, [0, 0.01],
              ['Possibility distributions', 'Updated possibility distributions using the reliability factor'],
              ['-', '--'], "FN14_p1_normalized.png")

# Tracer et sauvegarder la figure pour FN13_p1 avec un écart de 0.1
plot_and_save(file_path_FN13, [0, 0.1],
              ['Possibility distributions', 'Updated possibility distributions using the reliability factor'],
              ['-', '--'], "FN13_p1_normalized.png")

# Tracer et sauvegarder la figure pour FN7_p1 avec une ligne horizontale pour la courbe bleu ciel
plot_and_save(file_path_FN7, [0, 0],
              ['Possibility distributions', 'Updated possibility distributions using the reliability factor'],
              ['-', '--'], "FN7_p1_normalized.png")
