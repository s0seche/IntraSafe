from vulners import VulnersApi
import json

# Définir votre clé API
api_key = "B07YQ414IKEO3AN184VEJXKP3IXEYBL1XS9462WFQIEUH3XFJYNMDFN5Z741FY4D"

# Initialiser l'objet VulnersApi avec votre clé API
vulners_api = VulnersApi(api_key)

def list_apache_vulnerabilities(cible):
    try:
        # Récupérer les dernières vulnérabilités liées à Apache
        vulnerabilities = vulners_api.find(cible, limit=5)  # Limitez à 3 vulnérabilités pour cet exemple
        vuln_list = []
        # Afficher les vulnérabilités
        for vulnerability in vulnerabilities:
            vuln_data = {
                "CVE ID": vulnerability.get("id"),
                "Description": vulnerability.get("description"),
                "CVSS Score": vulnerability.get("cvss").get("score"),
                "References": vulnerability.get("references")
            }
            vuln_list.append(vuln_data)

        with open('vulnerabilities.json', 'w') as json_file:
            json.dump(vuln_list, json_file, indent=4)

    except Exception as e:
        print("Une erreur s'est produite lors de la recherche de vulnérabilités:", e)

# Appel de la fonction pour lister les vulnérabilités Apache
