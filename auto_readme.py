import os

def create_readme(directory):
    # Récupérer le nom du dossier
    folder_name = os.path.basename(directory)

    # Contenu du fichier README.md
    readme_content = f"# {folder_name}\n\nReplace this text with your own content."

    # Chemin complet du fichier README.md
    readme_file = os.path.join(directory, "README.md")

    # Créer le fichier README.md et écrire le contenu
    with open(readme_file, "w") as file:
        file.write(readme_content)

def main():
    # Obtenir le chemin du dossier courant
    current_directory = os.getcwd()

    # Parcourir les dossiers courants
    for directory in os.listdir(current_directory):
        # Vérifier si l'élément est un dossier
        if os.path.isdir(directory):
            create_readme(directory)

if __name__ == "__main__":
    main()
