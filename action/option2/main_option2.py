from action.option2.vuln_detection import list_apache_vulnerabilities

def option2_main():
    choix = 'y'

    while choix.lower() in ['y', 'yes']:
        cible = input(str("Services vulnérables à chercher ? "))
        list_apache_vulnerabilities(cible)
        choix = input(str("Voulez vous continuer ? "))
        print(choix)
