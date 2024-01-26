from pykeepass import PyKeePass
import openpyxl
import getpass

def charger_donnees(emplacement):
    if emplacement.endswith('.kdbx'):
        mot_de_passe = getpass.getpass("Veuillez entrer le mot de passe : ")

        try:
            with PyKeePass(emplacement, password=mot_de_passe) as kp:
                identifiants_mdp = {}
                for entry in kp.entries:
                    if entry.username and entry.password:
                        identifiants_mdp[entry.username] = entry.password

        except Exception as e:
            print(f"Erreur lors de l'extraction des identifiants du fichier kdbx: {e}")
            return None

    elif emplacement.endswith(('.xls', '.xlsx')):
        try:
            classeur = openpyxl.load_workbook(emplacement)
            feuille = classeur.active

            identifiants_mdp = {}
            for identifiant, mot_de_passe in zip(feuille['A'][1:], feuille['B'][1:]):
                if identifiant.value and mot_de_passe.value:
                    identifiants_mdp[identifiant.value] = mot_de_passe.value

        except Exception as e:
            print(f"Une erreur s'est produite lors du chargement du fichier Excel : {e}")
            return None

    else:
        print("Format de fichier non pris en charge.")
        return None

    return identifiants_mdp
