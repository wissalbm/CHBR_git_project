import csv
import os
import pandas as pd
from collections import defaultdict


def extract_failures(failures_file, failure_list):
    failures = []

    # Read the failure names from the Failures_Pk column
    with open(failures_file, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            failure_names = row['Failures_Pk'].split(',')
            for name in failure_names:
                failures.append([name.strip()])

    # Write the failure names into a new CSV file
    with open(failure_list, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['failureName'])  # Header
        writer.writerows(failures)

    print(f"Failure names have been extracted and saved into {failure_list}")
def extract_feature(feature_file, feature_list):
    # Lecture du fichier de fonctionnalités
    df = pd.read_csv(feature_file)

    # Extraction des primitives de la colonne "Symbols FN1-23/ FB1-7"
    feature_names = df["Symbols FN1-23/ FB1-7"].tolist()

    # Sauvegarde dans un fichier CSV avec une colonne nommée "feature_name"
    df_feature_names = pd.DataFrame({"feature_name": feature_names})
    df_feature_names.to_csv(feature_list, index=False)
def remplir_vecteur_failure(input_file):
    valeurs_P = set()  # Utiliser un ensemble pour stocker les valeurs uniques de la colonne failureName

    with open(input_file, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            valeur_failureName = row['failureName']
            valeurs_P.add(valeur_failureName)

    return sorted(valeurs_P)  # Retourner les valeurs triées par ordre alphabétique
def remplir_vecteur_feature(input_file):
    valeurs_P = set()  # Utiliser un ensemble pour stocker les valeurs uniques de la colonne failureName

    with open(input_file, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            valeur_featureName = row['feature_name']
            valeurs_P.add(valeur_featureName)

    return sorted(valeurs_P)  # Retourner les valeurs triées par ordre alphabétique
def create_HCB(input_file, output_folder, vecteur_V):
    # Créer les dossiers s'ils n'existent pas déjà
    if not os.path.exists(output_folder + "/CB_H/withPanne"):
        os.makedirs(output_folder + "/CB_H/withPanne")
    if not os.path.exists(output_folder + "/CB_H/withoutPanne"):
        os.makedirs(output_folder + "/CB_H/withoutPanne")

    for p_value in vecteur_V:
        lignes_P = []  # Initialiser une liste pour stocker les lignes contenant la valeur de P dans la dernière colonne
        lignes_non_P = []  # Initialiser une liste pour stocker les lignes ne contenant pas la valeur de P dans la dernière colonne

        with open(input_file, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)

            # Parcourir chaque ligne du fichier CSV
            for row in reader:
                last_column = row[-1].strip()  # Supprimer les espaces autour de la dernière colonne
                # Séparer les éléments de la dernière colonne en utilisant la virgule comme séparateur
                elements = last_column.split(", ")
                # Vérifier si la valeur de P est présente dans les éléments de la dernière colonne
                if p_value in elements:
                    lignes_P.append(row[:-1])  # Ajouter la ligne sans la dernière colonne à la liste des lignes contenant la valeur de P
                else:
                    lignes_non_P.append(row[:-1])  # Ajouter la ligne sans la dernière colonne à la liste des lignes ne contenant pas la valeur de P

        # Écrire les lignes contenant la valeur de P dans le dossier CB_H_withPanne
        with open(output_folder + f"/CB_H/withPanne/{p_value.lower()}.csv", 'w', newline='') as f1:
            writer = csv.writer(f1)
            for ligne in lignes_P:
                writer.writerow(ligne)

        # Écrire les lignes ne contenant pas la valeur de P dans le dossier CB_H_withoutPanne
        with open(output_folder + f"/CB_H/withoutPanne/{p_value.lower()}.csv", 'w', newline='') as f2:
            writer = csv.writer(f2)
            for ligne in lignes_non_P:
                writer.writerow(ligne)
def create_CB_H_LPF(source_folder, V, destination_folder):
    # Liste des fichiers dans le dossier source
    files_in_folder = os.listdir(source_folder)

    # Parcours de chaque fichier dans le dossier source
    for source_file_name in files_in_folder:
        # Chemin complet du fichier source
        source_file_path = os.path.join(source_folder, source_file_name)

        # Extraction du nom du fichier source
        source_file_base = os.path.splitext(source_file_name)[0]

        # Lecture du fichier contenant les lignes
        with open(source_file_path, 'r') as file:
            lignes = file.readlines()

        # Parcours de chaque élément du vecteur V
        for element in V:
            # Initialisation des fichiers de sortie
            with open(f'{source_file_base}_{element}_withpanne.csv', 'w', newline='') as withpanne_file, \
                    open(f'{source_file_base}_{element}_withoutpanne.csv', 'w', newline='') as withoutpanne_file:
                # Création des objets écrivains CSV
                withpanne_writer = csv.writer(withpanne_file)
                withoutpanne_writer = csv.writer(withoutpanne_file)

                # Parcours de chaque ligne
                for ligne in lignes:
                    # Division de la ligne en éléments
                    elements_ligne = ligne.strip().split(',')
                    # Vérification de l'existence exacte de l'élément dans la liste d'éléments de la ligne
                    if element in elements_ligne:
                        # Écriture dans le fichier avec "oui" en première colonne et la ligne en deuxième colonne
                        withpanne_writer.writerow( elements_ligne)
                    else:
                        # Écriture dans le fichier avec "non" en première colonne et la ligne en deuxième colonne
                        withoutpanne_writer.writerow( elements_ligne)

        # Création des dossiers "withpanne" et "withoutpanne" sous le dossier destination s'ils n'existent pas déjà
        for folder in [os.path.join(destination_folder, 'withpanne'), os.path.join(destination_folder, 'withoutpanne')]:
            if not os.path.exists(folder):
                os.makedirs(folder)

        # Liste des fichiers générés
        generated_files = os.listdir()

        # Parcours de chaque fichier généré
        for file_name in generated_files:
            # Si le fichier est un fichier de résultats avec panne
            if "_withpanne.csv" in file_name:
                # Déplacer et renommer le fichier dans le dossier withpanne avec le préfixe du nom du fichier source
                os.rename(file_name, os.path.join(destination_folder, 'withpanne', f'{file_name}'))
            # Si le fichier est un fichier de résultats sans panne
            elif "_withoutpanne.csv" in file_name:
                # Déplacer et renommer le fichier dans le dossier withoutpanne avec le préfixe du nom du fichier source
                os.rename(file_name, os.path.join(destination_folder, 'withoutpanne', f'{file_name}'))


# def process_files(file_p, CBRFile,primlist):
#     V_entete = ["FN1", "FN2", "FN3", "FN4", "FN5", "FN6", "FN7", "FN8", "FN9", "FN10", "FN11", "FN12", "FN13", "FN14",
#                 "FN15", "FN16", "FN17", "FN18", "FN19", "FN20", "FN21", "FN22", "FN23", "FB1", "FB2", "FB3", "FB4",
#                 "FB5", "FB6", "FB7"]
#
#     # Initialiser le vecteur V1
#     V1 = []
#
#     # Ouvrir le fichier CSV en mode lecture
#     with open(file_p, 'r') as fichier_csv:
#         # Créer un objet lecteur CSV
#         lecteur_csv = csv.reader(fichier_csv)
#
#         # Lire toutes les lignes du fichier
#         for ligne in lecteur_csv:
#             # Stocker les valeurs de la ligne dans V1
#             V1.extend(ligne)
#
#     # Afficher V1 pour vérification
#     print(V1)
#
#     # Initialiser une liste pour stocker les valeurs de V_value
#     V_value = []
#
#     # Ouvrir le fichier CSV en mode lecture
#     with open(CBRFile, 'r') as fichier_csv:
#         # Créer un objet lecteur CSV
#         lecteur_csv = csv.reader(fichier_csv)
#
#         # Lire toutes les lignes du fichier
#         for ligne in lecteur_csv:
#             # Stocker les valeurs de la ligne dans V_value
#             V_value.extend(ligne)
#
#     # Afficher V_value pour vérification
#     print(V_value)
#
#     # Initialisation d'une liste pour stocker les résultats
#     results = []
#
#     # Parcourir chaque élément de V1
#     for primitive in V1:
#         # Chercher l'index de la primitive dans V_entete
#         index = V_entete.index(primitive)
#         # Récupérer la valeur correspondante dans V_value
#         valeur = V_value[index]
#         # Ajouter le résultat à la liste des résultats
#         results.append({'nomprimitive': primitive, 'value': valeur})
#
#     # Créer un DataFrame pandas à partir des résultats
#     df = pd.DataFrame(results)
#
#     # Enregistrer dans un fichier CSV
#     df.to_csv(primlist, index=False)




def process_files(file_p, CBRFile, primlist):
    V_entete = ["FN1", "FN2", "FN3", "FN4", "FN5", "FN6", "FN7", "FN8", "FN9", "FN10", "FN11", "FN12", "FN13", "FN14",
                "FN15", "FN16", "FN17", "FN18", "FN19", "FN20", "FN21", "FN22", "FN23", "FB1", "FB2", "FB3", "FB4",
                "FB5", "FB6", "FB7"]

    # Initialiser le vecteur V1
    V1 = []

    # Ouvrir le fichier CSV en mode lecture
    with open(file_p, 'r') as fichier_csv:
        # Créer un objet lecteur CSV
        lecteur_csv = csv.reader(fichier_csv)

        # Lire toutes les lignes du fichier
        for ligne in lecteur_csv:
            # Stocker les valeurs de la ligne dans V1
            V1.extend(ligne)

    # Afficher V1 pour vérification
    print(V1)

    # Initialiser une liste pour stocker les valeurs de V_value
    V_value = []

    # Ouvrir le fichier CSV en mode lecture
    with open(CBRFile, 'r') as fichier_csv:
        # Créer un objet lecteur CSV
        lecteur_csv = csv.reader(fichier_csv)

        # Lire toutes les lignes du fichier
        for ligne in lecteur_csv:
            # Stocker les valeurs de la ligne dans V_value
            V_value.append(ligne)

    # Afficher V_value pour vérification
    print(V_value)

    # Initialisation d'une liste pour stocker les résultats
    results = []

    # Parcourir chaque élément de V1
    for i, primitive in enumerate(V1):
        # Récupérer l'index de la primitive dans V_entete
        index = V_entete.index(primitive)
        # Récupérer la valeur correspondante dans V_value pour la même ligne (même indice i) et le même index
        if i < len(V_value):  # Vérifier si l'indice est dans la plage de V_value
            valeur = V_value[i][index]
            # Ajouter le résultat à la liste des résultats
            results.append({'nomprimitive': primitive, 'value': valeur})
        else:
            break  # Arrêter la boucle si V_value est épuisé

    # Créer un DataFrame pandas à partir des résultats
    df = pd.DataFrame(results)

    # Enregistrer dans un fichier CSV
    df.to_csv(primlist, index=False)


def groupe_primitive_valueByName (primlist,vecteur ):
    # Charger le fichier CSV
    df = pd.read_csv(primlist)

    # Grouper les valeurs par nomprimitive et les stocker dans une nouvelle colonne 'grouped_values'
    grouped_data = df.groupby('nomprimitive')['value'].apply(list).reset_index(name='grouped_values')

    # Enregistrer le résultat dans un nouveau fichier CSV
    grouped_data.to_csv(vecteur, index=False)

