from action.option2.vuln_detection import list_vuln, print_pretty_json
import json
def option2_main():
    choix = 'y'

    while choix.lower() in ['y', 'yes']:
        cible = input(str("Services vulnérables à chercher ? "))
        list_vuln(cible)
            
        with open('vulnerabilities.json', 'r') as file:
            data = json.load(file)
        # Afficher les données JSON de manière jolie
        print_pretty_json(data)


        choix = input(str("Voulez vous continuer ? "))
        
