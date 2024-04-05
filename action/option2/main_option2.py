from action.option2.vuln_detection import list_apache_vulnerabilities

def option2_main():
    choix = "y"
    while choix == "yes" or "y":
        list_apache_vulnerabilities()
        choix = input(str("Avez vous d'autres vuln a chercher ? "))
        choix.lower 