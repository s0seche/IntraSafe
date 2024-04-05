import json


def afficher_param():
    # Charger le fichier JSON
    with open('../configuration/conf.json', 'r') as fichier:
        donnees = json.load(fichier)
    # Afficher toutes les paires clé-valeur
    for cle, valeur in donnees.items():
        print(f"{cle}: {valeur}")

afficher_param()

