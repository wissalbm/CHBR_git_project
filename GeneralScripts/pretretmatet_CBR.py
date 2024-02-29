
import pandas as pd
def remove_header_and_last_column(input_file, output_file):
    # Lecture du fichier CSV
    df = pd.read_csv(input_file)

    # Suppression de la première ligne
    df = df.iloc[1:]

    # Suppression de la dernière colonne nommée "label"
    if 'label' in df.columns:
        df.drop(columns=['label'], inplace=True)
    else:
        print("Aucune colonne nommée 'label' trouvée.")

    # Enregistrement dans un nouveau fichier
    df.to_csv(output_file, index=False)


def remove_header_and_save(input_file, output_file):
    # Lecture du fichier CSV sans l'entête
    df = pd.read_csv(input_file, header=None, skiprows=1)

    # Enregistrement dans un nouveau fichier
    df.to_csv(output_file, index=False, header=False)