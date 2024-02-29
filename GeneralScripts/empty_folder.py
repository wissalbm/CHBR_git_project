import os


def empty_folder(folder_path):
    # Vérifier si le chemin spécifié est un dossier
    if not os.path.isdir(folder_path):
        print(f"{folder_path} n'est pas un dossier valide.")
        return

    # Parcours récursif de tous les éléments du dossier
    for root, dirs, files in os.walk(folder_path, topdown=False):
        # Supprimer chaque fichier dans le dossier
        for file_name in files:
            file_path = os.path.join(root, file_name)
            os.remove(file_path)
        # Supprimer chaque dossier vide
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            os.rmdir(dir_path)

    print(f"Le dossier {folder_path} a été vidé avec succès.")



