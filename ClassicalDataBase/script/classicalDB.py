
import pandas as pd
import shutil

#create classical DB etiquity with statut
def label_vectors_classicalDB(failureFile, vectorStatutFile, DB_classicalCase_statut):
    # Charger les fichiers CSV
    failures_df = pd.read_csv(failureFile)
    vectors_df = pd.read_csv(vectorStatutFile)

    # Initialiser la colonne "label" à une chaîne vide pour tous les vecteurs
    vectors_df['label'] = ''

    # Parcourir chaque ligne du dataframe des pannes
    for _, failure_row in failures_df.iterrows():
        # Récupérer le nom de la panne et les primitives associées
        failure_pk = failure_row['Failures_Pk']
        primitives = failure_row['Primitives_FM'].split(',')

        # Parcourir chaque ligne du dataframe des vecteurs
        for index, vector_row in vectors_df.iterrows():
            # Vérifier si les primitives de la panne sont présentes dans le vecteur
            for prim in primitives:
                prim = prim.strip()
                if vector_row[prim] == 0:
                    # Si une primitive est absente dans le vecteur, étiqueter le vecteur avec le nom de la panne
                    if vectors_df.at[index, 'label'] == '':
                        vectors_df.at[index, 'label'] = failure_pk
                    else:
                        vectors_df.at[index, 'label'] += ',' + failure_pk
                    break  # Passer à la ligne suivante

    # Enregistrer le dataframe étiqueté dans un nouveau fichier CSV
    vectors_df.to_csv(DB_classicalCase_statut, index=False)



#create classical DB etiquity
def create_cassicalDB_step1(vecteurcsv_withEntete, classicalDB):
    # Copier le contenu du fichier source vers le fichier de destination
    shutil.copyfile(vecteurcsv_withEntete, classicalDB)

def create_cassicalDB_step2(classicalDB, DB_classicalCase_statut):
    # Charger les fichiers CSV
    source_df = pd.read_csv(classicalDB)
    label_df = pd.read_csv(DB_classicalCase_statut)

    # Ajouter la colonne 'label' du fichier de labels au fichier source
    source_df['label'] = label_df['label']

    # Copier le contenu du fichier source avec la nouvelle colonne vers le fichier de destination
    source_df.to_csv(classicalDB, index=False)

#add case name to the  classical database


def add_case_name_classicalDB(classicalDB, classicalDB_withNames):
    # Charger le fichier CSV
    df = pd.read_csv(classicalDB)

    # Ajouter une nouvelle colonne 'case_name' à l'indice 0
    df.insert(0, 'case_name', [f'case{i}' for i in range(1, len(df) + 1)])

    # Enregistrer le DataFrame modifié dans un nouveau fichier CSV
    df.to_csv(classicalDB_withNames, index=False)




