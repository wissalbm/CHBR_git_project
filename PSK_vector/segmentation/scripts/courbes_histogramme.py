import pandas as pd
import matplotlib.pyplot as plt
import os



def save_histogram_from_csv(csv_file, output_folder, color):
    # Charger le fichier CSV
    df = pd.read_csv(csv_file)

    # Convertir les chaînes de caractères en listes
    df['grouped_values'] = df['grouped_values'].apply(eval)

    # Créer un dictionnaire pour stocker le nombre d'éléments par primitive
    counts = {row['nomprimitive']: len(row['grouped_values']) for _, row in df.iterrows()}

    # Tracer l'histogramme
    plt.bar(counts.keys(), counts.values(), color=color)

    # Ajouter des labels et un titre
    plt.xlabel('Primitive')
    plt.ylabel('Nombre de valeurs')
    plt.title('Histogramme du nombre de valeurs par primitive')

    # Afficher le graphique
    plt.xticks(rotation=90)  # Rotation des labels de l'axe des x pour une meilleure lisibilité
    plt.tight_layout()  # Ajustement automatique de la mise en page

    # Vérifier si le dossier de sortie existe, sinon le créer
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Construire le chemin de sortie pour sauvegarder le graphique
    output_filename = os.path.splitext(os.path.basename(csv_file))[0] + '.png'
    output_path = os.path.join(output_folder, output_filename)

    # Enregistrer le graphique
    plt.savefig(output_path)

    # Afficher le nom du fichier sauvegardé
    print(f"Le graphique a été sauvegardé sous : {output_path}")

    # Fermer le graphique
    plt.close()

def save_histogram_plot(csv_file, output_folder, color):
    # Charger le fichier CSV
    df = pd.read_csv(csv_file)

    # Convertir les chaînes de caractères en listes
    df['grouped_values'] = df['grouped_values'].apply(eval)

    # Créer un dictionnaire pour stocker le nombre d'éléments par primitive
    counts = {row['nomprimitive']: len(row['grouped_values']) for _, row in df.iterrows()}

    # Trier les valeurs par clé
    sorted_counts = dict(sorted(counts.items()))

    # Extraire les clés et les valeurs triées
    keys = list(sorted_counts.keys())
    values = list(sorted_counts.values())

    # Tracer la courbe
    plt.plot(keys, values, color=color, marker='o', linestyle='-')

    # Ajouter des labels et un titre
    plt.xlabel('Primitive')
    plt.ylabel('Nombre de valeurs')
    plt.title('Histogramme du nombre de valeurs par primitive')

    # Afficher le graphique
    plt.xticks(rotation=90)  # Rotation des labels de l'axe des x pour une meilleure lisibilité
    plt.tight_layout()  # Ajustement automatique de la mise en page

    # Normaliser l'échelle de l'axe des ordonnées
    plt.ylim(0, max(values) * 1.1)  # Augmenter légèrement la limite supérieure pour éviter les coupures

    # Vérifier si le dossier de sortie existe, sinon le créer
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Construire le chemin de sortie pour sauvegarder le graphique
    output_filename = os.path.splitext(os.path.basename(csv_file))[0] + '.png'
    output_path = os.path.join(output_folder, output_filename)

    # Enregistrer le graphique
    plt.savefig(output_path)

    # Afficher le nom du fichier sauvegardé
    print(f"Le graphique a été sauvegardé sous : {output_path}")

    # Fermer le graphique
    plt.close()


