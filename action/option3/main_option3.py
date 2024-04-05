from action.option3.analyse import analyser_mots_de_passe
from action.option3.donnes import charger_donnees


def option3_main():
    choix = 'y'
    while choix.lower() == 'y'or choix == 'yes':

        emplacement_fichier = input("Veuillez entrer le chemin complet du fichier .xlsx  .kdbx: ")
        donnees = charger_donnees(emplacement_fichier)

        if donnees:
            print("\nAnalyse des mots de passe :")
            for mot_de_passe in donnees.values():
                analyser_mots_de_passe(mot_de_passe)
                
        choix = input("Voulez-vous analyser d'autres mots de passe ? (y/n): ")
    