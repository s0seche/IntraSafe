import openpyxl

def charger_donnees_ods(emplacement):
    try:
        # Chargement du fichier .ods
        classeur = openpyxl.load_workbook(emplacement)
        # Sélection de la première feuille
        feuille = classeur.active

        # Extraction de la colonne "identifiant" et "pass" dans un dictionnaire
        donnees_utilisateurs = {}
        colonne_identifiant = feuille['A']
        colonne_pass = feuille['B']

        for identifiant, mot_de_passe in zip(colonne_identifiant[1:], colonne_pass[1:]):
            if identifiant.value and mot_de_passe.value:
                donnees_utilisateurs[identifiant.value] = mot_de_passe.value

        return donnees_utilisateurs

    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return None
