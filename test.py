import pandas as pd
import os

def extraire_valeurs_occurrences(input_file, output_file):
    # Lire le fichier CSV
    df = pd.read_csv(input_file)

    # Extraire les valeurs distinctes de la colonne "val" et compter le nombre d'occurrences
    occurrences = df['val'].value_counts()

    # Écrire les valeurs et leurs occurrences dans un nouveau fichier CSV
    occurrences.to_csv(output_file, header=['occurrences'], index_label='value')

def appliquer_compter_occurences_sur_dossiers_feauture(folder_path, output_folder):
    # Créer le dossier 'courbefiles' s'il n'existe pas
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Parcourir les fichiers dans le dossier spécifié
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('_Value.csv'):
                file_path = os.path.join(root, file)
                output_file = os.path.join(output_folder, file.replace('withpanne_', ''))
                extraire_valeurs_occurrences(file_path, output_file)

# Exemple d'utilisation de la fonction
folder_path = "PSK_vector/segmentation/sub_databases/groupe/Panne/"
output_folder = "PSK_vector/segmentation/sub_databases/groupe/Panne/courbefiles/"
appliquer_compter_occurences_sur_dossiers_feauture(folder_path, output_folder)
