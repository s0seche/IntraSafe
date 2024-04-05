import json
def lire_informations(fichier_texte):
    informations = {}
    with open(fichier_texte, 'r', encoding='utf-8') as fichier:
        for ligne in fichier:
            if ":" in ligne:
                cle, valeur = ligne.strip().split(":", 1)
                cle = cle.strip()
                valeur = valeur.strip()
                informations[cle] = valeur
    return informations

def creer_fichier(informations, chemin_fichier_json):
    with open(chemin_fichier_json, 'w', encoding='utf-8') as fichier:
        json.dump(informations, fichier, indent=4)

fichier_texte = 'configuration.txt'
chemin_fichier_json = 'configuration/conf.json'

