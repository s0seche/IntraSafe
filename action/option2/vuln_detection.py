from vulners import VulnersApi

# Définir votre clé API
api_key = "B07YQ414IKEO3AN184VEJXKP3IXEYBL1XS9462WFQIEUH3XFJYNMDFN5Z741FY4D"

# Initialiser l'objet VulnersApi avec votre clé API
vulners_api = VulnersApi(api_key)

def list_apache_vulnerabilities():
    cible = input(str("Vuln ? "))
    try:
        # Récupérer les dernières vulnérabilités liées à Apache
        vulnerabilities = vulners_api.find(cible, limit=3)  # Limitez à 10 vulnérabilités pour cet exemple

        # Afficher les vulnérabilités
        for vulnerability in vulnerabilities:
            print("CVE ID:", vulnerability.get("id"))
            print("Description:", vulnerability.get("description"))
            print("CVSS Score:", vulnerability.get("cvss").get("score"))
            print("References:", vulnerability.get("references"))
            print()
    except Exception as e:
        print("Une erreur s'est produite lors de la recherche de vulnérabilités:", e)

# Appel de la fonction pour lister les vulnérabilités Apache
