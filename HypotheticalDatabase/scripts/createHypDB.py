import csv
import random

import pandas as pd


#def pour trouver les primitives les plus importants : pour savoir nous parcourons le fichier de la base des cas classiques et
# nous calculons le nbre d'apparition des primitives pour l'ensemble des pannes trouv�es
def count_nbre_appartenance(DB_classicalCasestatut, membership_primitives):
    zero_counts = {}

    # Open the CSV file
    with open(DB_classicalCasestatut, 'r') as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)  # Get the header

        # Initialize zero counts for all columns excluding "label"
        for col in header:
            if col != 'label':
                zero_counts[col] = 0

        # Count zeros for each column excluding "label"
        for row in reader:
            for col_idx, value in enumerate(row):
                if header[col_idx] != 'label' and value == '0':
                    zero_counts[header[col_idx]] += 1

    # Write results to a new CSV file
    with open(membership_primitives, 'w', newline='') as output_csv:
        writer = csv.writer(output_csv)
        writer.writerow(['primitives', 'nbr_appearances'])
        for col, count in zero_counts.items():
            writer.writerow([col, count])

# trier la liste des primitives selon le nombre trouvé : la valeurs la plus grande = la primitives la plus importantes
def trie_appartenanceFile(membership_primitives, membership_primitives_trie):
    # Charger le fichier CSV
    df = pd.read_csv(membership_primitives)

    # Trier le DataFrame selon la colonne 'nbr_appearances' par ordre d�croissant
    df_sorted = df.sort_values(by='nbr_appearances', ascending=False)

    # Sauvegarder le r�sultat tri� dans un nouveau fichier CSV
    df_sorted.to_csv(membership_primitives_trie, index=False)

#calculer le poid les primitives selon les pannes : on regarde quelle sont les causes des pannes
#nous avons 3 cat�gories :
#     1: poid plus fort primitive qui apparait dans la plus part des pannes (figure dans plusieurs pannes)
#     2: poid qui figure dans mois de 2 pannes
#     3: n'existe pas dans la liste des pannes


def assign_weights(sourceFile_Failures_CSV, weight_primitive):
    # Lecture du fichier CSV
    df = pd.read_csv(sourceFile_Failures_CSV)

    # Compter le nombre d'occurrences de chaque primitive
    primitive_counts = df['Primitives_FM'].str.split(',').explode().str.strip().value_counts()

    # Créer un DataFrame pour stocker les résultats
    result = pd.DataFrame({
        'primitive_name': primitive_counts.index,
        'poid_primitive': primitive_counts.apply(lambda x: 2 if x == 1 else 1)
    })

    # Enregistrement du résultat dans un nouveau fichier CSV
    result.to_csv(weight_primitive, index=False)

# Generate vectors of primitives (random order, 10 < number < 30)


def generate_vector(vector_HBR, num_vectors=100):
    # Vecteur contenant toutes les primitives FN et FB sauf FN14, FN18, FB5
    vecteur = ["FN1", "FN2", "FN3", "FN4", "FN5", "FN6", "FN7", "FN8", "FN9", "FN10", "FN11", "FN12", "FN13",
               "FN15", "FN16", "FN17", "FN19", "FN20", "FN21", "FN22", "FN23", "FB1", "FB2", "FB3", "FB4",
               "FB6", "FB7"]

    # Ouvrir le fichier CSV en mode append pour ajouter des lignes
    with open(vector_HBR, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)

        for _ in range(num_vectors):
            # Initialiser la séquence avec FN14, FN18, FB5
            sequence = ["FN14", "FN18", "FB5"]

            # Générer un nombre aléatoire entre 7 et 27 pour déterminer le nombre de primitives restantes à extraire
            remaining_primitives = random.randint(7, 27)

            # Sélection aléatoire de primitives du vecteur restantes
            random_primitives = random.sample(vecteur, remaining_primitives)

            # Ajouter les primitives restantes à la séquence
            sequence.extend(random_primitives)

            # Écrire la séquence dans le fichier CSV
            writer.writerow(sequence)

    print(f"{num_vectors} vecteurs ont été ajoutés au fichier {vector_HBR}.")

def reorder_primitives_by_membership(vector_HBR_file, membership_file, vector_HBR_tri_membership):
    # Lire les données de nombre d'apparitions des primitives depuis le fichier de membership
    primitives_appearances = {}
    with open(membership_file, 'r') as membership_csv:
        reader = csv.DictReader(membership_csv)
        for row in reader:
            primitives_appearances[row['primitives']] = int(row['nbr_appearances'])

    # Fonction de comparaison pour le tri des primitives dans chaque ligne du vecteur
    def compare_primitives(primitive):
        return primitives_appearances.get(primitive, 0)

    # Ouvrir le fichier CSV en mode lecture et écriture
    with open(vector_HBR_file, 'r', newline='') as input_csv, \
            open(vector_HBR_tri_membership, 'w', newline='') as output_csv:
        reader = csv.reader(input_csv)
        writer = csv.writer(output_csv)

        # Lire chaque ligne du fichier d'entrée, réorganiser les primitives et écrire dans le fichier de sortie
        for row in reader:
            # Conserver les trois premières primitives intactes
            first_three_primitives = row[:3]
            # Tri des primitives restantes
            reordered_primitives = sorted(row[3:], key=compare_primitives, reverse=True)
            # Reconstruire la ligne en conservant les trois premières primitives inchangées
            reordered_row = first_three_primitives + reordered_primitives
            writer.writerow(reordered_row)

    print(f"Les primitives ont été réorganisées dans chaque ligne et sauvegardées dans {vector_HBR_tri_membership}.")


def map_vector_failure(vector_HBR_tri_membership,failuresFile,HBR_vectors_with_FailureName ):

        # Créer un dictionnaire pour stocker les pannes associées à chaque primitive
        primitive_failures = {}

        # Lire le fichier failuresFile et remplir le dictionnaire primitive_failures
        with open(failuresFile, 'r') as failures_csv:
            reader = csv.DictReader(failures_csv)
            for row in reader:
                failures = row['Primitives_FM'].split(',')
                for failure in failures:
                    failure = failure.strip()
                    if failure not in primitive_failures:
                        primitive_failures[failure] = []
                    primitive_failures[failure].append(row['Failures_Pk'])

        # Ouvrir le fichier pour écrire les résultats
        with open(HBR_vectors_with_FailureName, 'w', newline='') as output_csv:
            writer = csv.writer(output_csv)

            # Lire le fichier vector_HBR_tri_membership ligne par ligne
            with open(vector_HBR_tri_membership, 'r', newline='') as input_csv:
                reader = csv.reader(input_csv)
                for row in reader:
                    # Créer une liste pour stocker les pannes associées à chaque vecteur
                    vector_failures = []
                    # Parcourir chaque primitive dans le vecteur
                    for primitive in row:
                        if primitive in primitive_failures:
                            vector_failures.extend(primitive_failures[primitive])

                    # Écrire le vecteur avec les pannes associées dans le fichier de sortie
                    writer.writerow(row + [", ".join(set(vector_failures))])

        print("Le mapping des pannes avec les vecteurs a été effectué avec succès.")


def create_HDB_file(ClassicalDataBase, vector_HBR_tri_membership, HypotheticalDatabaseFile):
    # Lire les données du fichier ClassicalDataBase et stocker les valeurs correspondantes pour chaque primitive
    primitive_values = {}
    with open(ClassicalDataBase, 'r') as classical_file:
        reader = csv.DictReader(classical_file)
        for row in reader:
            for primitive, value in row.items():
                if primitive != 'label':
                    primitive_values[primitive] = value

    # Ouvrir le fichier vector_HBR_tri_membership pour lecture et HDB_file pour écriture
    with open(vector_HBR_tri_membership, 'r') as vector_file, \
            open(HypotheticalDatabaseFile, 'w', newline='') as hdb_output:
        reader = csv.reader(vector_file)
        writer = csv.writer(hdb_output)

        # Lire chaque ligne du fichier vector_HBR_tri_membership et remplacer les primitives par leurs valeurs correspondantes
        for row in reader:
            replaced_row = []
            for primitive in row:
                if primitive in primitive_values:
                    replaced_row.append(primitive_values[primitive])
                else:
                    replaced_row.append("FAUX")  # Valeur par défaut si la primitive n'est pas trouvée
            writer.writerow(replaced_row)

    print(f"Le fichier HDB a été créé avec succès : {HypotheticalDatabaseFile}")





def label_HDB(HypotheticalDatabaseFile_names, HBR_vectors_with_Failurevalues, HypotheticalDatabaseFile_withlabel):
    # Lire la dernière colonne du fichier names_file
    with open(HypotheticalDatabaseFile_names, 'r') as names_csv:
        reader = csv.reader(names_csv)
        last_column = [row[-1] for row in reader]

    # Lire les valeurs du fichier values_file
    with open(HBR_vectors_with_Failurevalues, 'r') as values_csv:
        reader = csv.reader(values_csv)
        data = list(reader)

    # Ajouter la dernière colonne à la liste des valeurs
    for i in range(len(data)):
        data[i].append(last_column[i])

    # Écrire les données dans le fichier de sortie
    with open(HypotheticalDatabaseFile_withlabel, 'w', newline='') as output_csv:
        writer = csv.writer(output_csv)
        writer.writerows(data)

    print(f"La dernière colonne a été copiée avec succès et enregistrée dans {HypotheticalDatabaseFile_withlabel}")
