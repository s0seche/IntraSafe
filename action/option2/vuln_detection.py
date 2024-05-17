from vulners import VulnersApi
import json

# clé API Vulner
api_key = "GAMNRV2MFM5JVEQPXWPRBU83HPKXR0RV6YTY38NFCWNSZHR0AMX2CC6DLFUB4ADQ"

vulners_api = VulnersApi(api_key)

def list_vuln(cible):
    try:
        vulnerabilities = vulners_api.find(cible, limit=5)  # Limitez à 5 vuln
        vuln_list = []
        # Afficher les vuln
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


def print_pretty_json(data, indent=0):
    for item in data:
        print('\t' * indent + "CVE ID:", item.get("CVE ID"))
        print('\t' * indent + "Description:", item.get("Description"))
        print('\t' * indent + "CVSS Score:", item.get("CVSS Score"))
        references = item.get("References")
        if references:
            print('\t' * indent + "References:")
            for reference in references:
                print('\t' * (indent + 1) + reference)
        else:
            print('\t' * indent + "References: None")
