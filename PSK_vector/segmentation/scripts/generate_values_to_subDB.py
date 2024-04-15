import shutil

import random
import pandas as pd
import os
import csv
from collections import Counter

def regroupe_according_Feature(base_dir,output_dir):
    # Supprimer le dossier de sortie s'il existe déjà
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)

    # Créer le dossier de sortie
    os.makedirs(output_dir)

    # Parcourir le dossier de base
    for file_name in os.listdir(base_dir):
        if file_name.endswith(".csv"):
            panne, feature = file_name.split("_")[0][1:], file_name.split("_")[1]
            feature_dir = os.path.join(output_dir, feature)
            # Créer un dossier pour chaque feature s'il n'existe pas
            if not os.path.exists(feature_dir):
                os.makedirs(feature_dir)
            # Copier le fichier dans le dossier correspondant
            shutil.copy(os.path.join(base_dir, file_name), feature_dir)
def regroupe_according_Panne(base_dir,output_dir):


    # Supprimer le dossier de sortie s'il existe déjà
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)

    # Créer le dossier de sortie
    os.makedirs(output_dir)

    # Parcourir le dossier de base
    for file_name in os.listdir(base_dir):
        if file_name.endswith(".csv"):
            panne, feature = file_name.split("_")[0], file_name.split("_")[1][1:]
            panne_dir = os.path.join(output_dir, panne)
            # Créer un dossier pour chaque panne s'il n'existe pas
            if not os.path.exists(panne_dir):
                os.makedirs(panne_dir)
            # Copier le fichier dans le dossier correspondant
            shutil.copy(os.path.join(base_dir, file_name), panne_dir)

# générer des valeurs sans la loi normale et binomiale
def create_values_forFeature(primitivesFile, generatesVectors):
    # Ouvrir le fichier source avec l'encodage UTF-8
    with open(primitivesFile, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        headers = reader.fieldnames

        # Vérifier si la colonne 'Symbols FN1-23/ FB1-7' existe
        if 'Symbols FN1-23/ FB1-7' in headers:
            # Créer le fichier de sortie et écrire les en-têtes
            with open(generatesVectors, mode='w', newline='', encoding='utf-8') as output_csv:
                writer = csv.writer(output_csv)
                writer.writerow(["Feature", "Vector"])

                # Parcourir chaque ligne du fichier source
                for row in reader:

                    symbol_value = row['Symbols FN1-23/ FB1-7']

                    # Générer le vecteur selon le préfixe de la valeur de la colonne
                    if symbol_value.startswith("FN"):
                        lower_limit = float(row['Lower_Limit'])
                        upper_limit = float(row['Upper_Limit'])

                        if symbol_value == "FN14":
                            # Pour FN14, laisser deux valeurs après la virgule
                            values = [round(random.uniform(lower_limit, upper_limit), 2) for _ in range(10)]
                        else:
                            # Enlever les chiffres après la virgule
                            lower_limit = int(lower_limit)
                            upper_limit = int(upper_limit)
                            values = [random.randint(lower_limit, upper_limit) for _ in range(10)]

                    elif symbol_value.startswith("FB"):
                        true_value = row['TruthValue']
                        false_value = row['FalseValue']
                        values = [true_value] * 7 + [false_value] * 3

                    # Écrire le nom de la fonction et le vecteur dans le fichier de sortie
                    writer.writerow([symbol_value, values])


# générer les valeurs avec loi normale et binomiale
# def moyenne(a, b):
#     return (a + b) / 2
#
# def ecart_type(a, b):
#     moy = moyenne(a, b)
#     ecart_a = (a - moy) ** 2
#     ecart_b = (b - moy) ** 2
#     variance = (ecart_a + ecart_b) / 2
#     return np.sqrt(variance)
#
# def generer_valeurs_normales(moyenne, ecart_type, nombre_valeurs):
#     if moyenne == int(moyenne):
#         moyenne = int(moyenne)
#     if ecart_type == int(ecart_type):
#         ecart_type = int(ecart_type)
#     return np.round(np.random.normal(moyenne, ecart_type, nombre_valeurs), 2)
#
# def create_values_forFeature(primitivesFile, generatesVectors):
#     # Ouvrir le fichier source avec l'encodage UTF-8
#     with open(primitivesFile, mode='r', newline='', encoding='utf-8') as file:
#         reader = csv.DictReader(file)
#         headers = reader.fieldnames
#
#         # Vérifier si la colonne 'Symbols FN1-23/ FB1-7' existe
#         if 'Symbols FN1-23/ FB1-7' in headers:
#             # Créer le fichier de sortie et écrire les en-têtes
#             with open(generatesVectors, mode='w', newline='', encoding='utf-8') as output_csv:
#                 writer = csv.writer(output_csv)
#                 writer.writerow(["Feature", "Vector"])
#
#                 # Parcourir chaque ligne du fichier source
#                 for row in reader:
#
#                     symbol_value = row['Symbols FN1-23/ FB1-7']
#
#                     # Générer le vecteur selon le préfixe de la valeur de la colonne
#                     if symbol_value.startswith("FN"):
#                         lower_limit = float(row['Lower_Limit'])
#                         upper_limit = float(row['Upper_Limit'])
#
#                         moy = moyenne(lower_limit, upper_limit)
#                         et = ecart_type(lower_limit, upper_limit)
#                         values = generer_valeurs_normales(moy, et, 10)
#
#                     elif symbol_value.startswith("FB"):
#                         true_value = row['TruthValue']
#                         false_value = row['FalseValue']
#                         values = [true_value] * 7 + [false_value] * 3
#
#                     # Écrire le nom de la fonction et le vecteur dans le fichier de sortie
#                     writer.writerow([symbol_value, values])
#

def generate_value_forGroup_features(directory):
    source_file = "sourceFiles/randomValue_forFeatureVector.csv"

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".csv"):
                file_path = os.path.join(root, file)

                # Extract feature name from file name
                feature_name = file.split("_")[1]

                # Read source value file
                source_df = pd.read_csv(source_file)

                # Read input CSV file
                with open(file_path, 'r') as input_file:
                    lines = input_file.readlines()

                # Create output CSV file
                output_file_path = os.path.join(root, f"{file.split('_')[0]}_Value.csv")
                with open(output_file_path, 'w') as output_file:
                    output_file.write("feat,val\n")
                    for line in lines:
                        features = line.strip().split(",")
                        if feature_name in features:
                            # Find value for feature from source file
                            feature_value = source_df.loc[source_df['Feature'] == feature_name, 'Vector'].values[0]
                            # Choose a random value from the vector
                            random_value = random.choice(feature_value.split(","))
                            output_file.write(f"{feature_name},{random_value}\n")


def generate_value_forGroup_pannes(directory):
    # Parcourir les dossiers et sous-dossiers
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.csv'):
                # Lire le nom de fichier
                filename = os.path.splitext(file)[0]
                # Extraire le nom de feature
                feature = filename.split('_')[1]

                # Ouvrir le fichier CSV
                with open(os.path.join(root, file), 'r') as csvfile:
                    reader = csv.reader(csvfile)

                    # Créer un nouveau fichier avec le même nom et '_value' ajouté
                    new_file = filename + '_Value.csv'
                    with open(os.path.join(root, new_file), 'w', newline='') as new_csvfile:
                        fieldnames = ['feature', 'val']
                        writer = csv.DictWriter(new_csvfile, fieldnames=fieldnames)

                        writer.writeheader()

                        # Parcourir le fichier ligne par ligne
                        for row in reader:
                            # Chercher la variable "feature"
                            if feature in row:
                                # Ouvrir le fichier "sourceFiles/randomValue_forFeatureVector.csv"
                                with open('sourceFiles/randomValue_forFeatureVector.csv', 'r') as random_csvfile:
                                    random_reader = csv.DictReader(random_csvfile)

                                    # Chercher la variable "feature" dans la colonne "Feature"
                                    for random_row in random_reader:
                                        if random_row['Feature'] == feature:
                                            # Sélectionner une valeur du vecteur de la colonne "Vector" de manière aléatoire
                                            val = random.choice(random_row['Vector'].split(','))

                                            # Écrire dans le nouveau fichier
                                            writer.writerow({'feature': feature, 'val': val})
                                            break  # Sortir de la boucle une fois la valeur trouvée

def nettoyer_colonne(file_path):
    # Définir les caractères à supprimer
    chars_to_remove = ['[', ']', "'", ' ']

    # Ouvrir le fichier CSV en mode lecture
    with open(file_path, mode='r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)  # Stocker les lignes dans une liste

    # Nettoyer la colonne "val" pour chaque ligne
    for row in rows:
        val = row['val']
        for char in chars_to_remove:
            val = val.replace(char, '')
        row['val'] = val

    # Réécrire les données dans le même fichier
    with open(file_path, mode='w', newline='') as csvfile:
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    # print(f"Les données nettoyées ont été enregistrées dans '{file_path}'.")

def nettoyer_tous_les_csv(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('_Value.csv'):
                file_path = os.path.join(root, file)
                nettoyer_colonne(file_path)

# préparer les fichiers de données pour tracers les courbes
def compter_occurences_feature(file_path):
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
    output_folder = os.path.join(folder_path, '..', 'courbefiles_feature')
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

    # print(f"Les résultats ont été enregistrés dans '{output_file_path}'.")

def appliquer_compter_occurences_sur_dossiers_feature(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('_Value.csv'):
                file_path = os.path.join(root, file)
                compter_occurences_feature(file_path)


# préparer les fichiers de données pour tracers les courbes
def extraire_valeurs_occurrences_pannes(input_file, output_file):
    # Lire le fichier CSV
    df = pd.read_csv(input_file)

    # Extraire les valeurs distinctes de la colonne "val" et compter le nombre d'occurrences
    occurrences = df['val'].value_counts()

    # Écrire les valeurs et leurs occurrences dans un nouveau fichier CSV
    occurrences.to_csv(output_file, header=['occurrences'], index_label='value')

def appliquer_compter_occurences_sur_dossiers_pannes(folder_path, output_folder):
    # Créer le dossier 'courbefiles' s'il n'existe pas
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Parcourir les fichiers dans le dossier spécifié
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('_Value.csv'):
                file_path = os.path.join(root, file)
                output_file = os.path.join(output_folder, file.replace('withpanne_', ''))
                extraire_valeurs_occurrences_pannes(file_path, output_file)


# # Appel de la fonction pour regrouper les fichiers Feature
# base_dir = "PSK_vector/segmentation/sub_databases/CB_H_LPF/withpanne"
# groupe_files_byFeatures= "PSK_vector/segmentation/sub_databases/groupe/Feature"
# regroupe_according_Feature(base_dir, groupe_files_byFeatures)
#
# # Appel de la fonction pour regrouper les fichiers Panne
# base_dir = "PSK_vector/segmentation/sub_databases/CB_H_LPF/withpanne"
# groupe_files_bypannes = "PSK_vector/segmentation/sub_databases/groupe/Panne"
# regroupe_according_Panne(base_dir,groupe_files_bypannes)
#
# # Appel de la fonction pour créer les valeurs aléatoires des Feature
# primitivesFile = "sourceFiles/primitives.csv"
# generatesVectors = "sourceFiles/randomValue_forFeatureVector.csv"
# create_values_forFeature(primitivesFile,generatesVectors)
#
# # Cas 1 : extract primitive value primitive in panne
# FeatureGroup = "PSK_vector/segmentation/sub_databases/groupe/Feature"
# generate_value_forGroup_features(FeatureGroup)
#
# # cas 2 : extract primitive value selon la panne with primitive
# PanneGroup = "PSK_vector/segmentation/sub_databases/groupe/Panne"
# generate_value_forGroup_pannes(PanneGroup)
#
# # netoyer la colonne val dans tous les fichiersFeature
# folder_path_Feature = "PSK_vector/segmentation/sub_databases/groupe/Feature"
# nettoyer_tous_les_csv(folder_path_Feature)
#
#
# # netoyer la colonne val dans tous les fichiers Panne
# folder_path_Panne = "PSK_vector/segmentation/sub_databases/groupe/Panne"
# nettoyer_tous_les_csv(folder_path_Panne)
#
#
#
# # création des fichiers de données pour feature
# folder_path_feature = "PSK_vector/segmentation/sub_databases/groupe/Feature"
# appliquer_compter_occurences_sur_dossiers_feauture(folder_path_feature)
#
# # création des fichiers de données pour pannes
# folder_path_Panne = "PSK_vector/segmentation/sub_databases/groupe/Panne/"
# output_folder_panne = "PSK_vector/segmentation/sub_databases/groupe/Panne/courbefiles_pannes/"
# appliquer_compter_occurences_sur_dossiers_pannes(folder_path_Panne, output_folder_panne)