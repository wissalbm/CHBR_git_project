import os


def empty_folder(folder):
    # Check if the folder exists
    if os.path.exists(folder):
        # List all files in the folder
        files = os.listdir(folder)

        # Check if there are any files in the folder
        if files:
            # Iterate over all files and delete them one by one
            for file in files:
                file_path = os.path.join(folder, file)
                os.remove(file_path)

            print(f"The files in the folder '{folder}' have been deleted.")
        else:
            print(f"The folder '{folder}' is empty.")
    else:
        print(f"The folder '{folder}' does not exist.")


