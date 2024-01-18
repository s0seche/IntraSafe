import openpyxl

def lire_fichier_ods(emplacement):
    try:
        # Chargement du fichier .ods
        classeur = openpyxl.load_workbook(emplacement)
        # Sélection de la première feuille
        feuille = classeur.active
        # Affichage du contenu
        """
        for ligne in feuille.iter_rows():
            for cellule in ligne:
                print(cellule.value, end='\t')
            print()
        """

        # Extraction de la colonne "identifiant" et "pass" dans un dictionnaire
        donnees_utilisateurs = {}
        colonne_identifiant = feuille['A']
        colonne_pass = feuille['B']

        for identifiant, mot_de_passe in zip(colonne_identifiant[1:], colonne_pass[1:]):
            print(identifiant.value)
            if identifiant.value != "" :
                donnees_utilisateurs[identifiant.value] = mot_de_passe.value
           
        valeur_test = donnees_utilisateurs['belje']
        i=0
        for identifiant.value in donnees_utilisateurs:
            print(identifiant.value)
        # Affichage du dictionnaire
        print("Données sous forme de dictionnaire :")

        print(donnees_utilisateurs)

    except Exception as e:
        print(f"Une erreur s'est produite : {e}")


#PS à retirer lors éxécution main
if __name__ == "__main__":
    emplacement_fichier = input("Veuillez entrer le chemin complet du fichier .ods : ")
    lire_fichier_ods(emplacement_fichier)
