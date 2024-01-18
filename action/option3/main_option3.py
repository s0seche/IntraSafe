from action.option3.open_file import charger_donnees_ods
from action.option3.analyse import analyser_mots_de_passe


def option3_main():
    emplacement_fichier = input("Veuillez entrer le chemin complet du fichier .ods : ")

    # Charger les données
    donnees = charger_donnees_ods(emplacement_fichier)

    if donnees:
        print("Données extraites :")
        print(donnees)

        # Analyser les mots de passe
        print("\nAnalyse des mots de passe :")
        for mot_de_passe in donnees.values():
            analyser_mots_de_passe(mot_de_passe)
