import os
import csv
from collections import Counter

def compter_occurences(file_path):
    # Ouvrir le fichier CSV en mode lecture
    with open(file_path, mode='r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        values = [row['val'] for row in reader]

    # Compter les occurrences de chaque valeur
    value_counts = Counter(values)

    # Créer le chemin pour le nouveau fichier
    folder_path = os.path.dirname(file_path)
    parent_folder = os.path.basename(folder_path)
    file_name = os.path.basename(file_path)
    prefix = file_name.split('_')[0]  # Extraire le préfixe du nom du fichier
    output_folder = os.path.join(folder_path, '..', 'courbefiles')
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    output_file_path = os.path.join(output_folder, f'{parent_folder}_{prefix}.csv')

    # Écrire les résultats dans le nouveau fichier
    with open(output_file_path, mode='w', newline='') as csvfile:
        fieldnames = ['Value', 'Occurrences']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for val, count in value_counts.items():
            writer.writerow({'Value': val, 'Occurrences': count})

    print(f"Les résultats ont été enregistrés dans '{output_file_path}'.")

def appliquer_compter_occurences_sur_dossiers(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('_Value.csv'):
                file_path = os.path.join(root, file)
                compter_occurences(file_path)

# Exemple d'utilisation de la fonction
folder_path = "PSK_vector/segmentation/sub_databases/groupe/Feature"
appliquer_compter_occurences_sur_dossiers(folder_path)
