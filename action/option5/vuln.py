import requests
from bs4 import BeautifulSoup
def vuln_web():
        
    # Fonction pour détecter les failles XSS
    def detect_xss(url):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            # Recherche de balises potentiellement vulnérables
            vulnerable_tags = soup.find_all(['script', 'iframe', 'img', 'input'])

            if vulnerable_tags:
                print("Vulnérabilités XSS détectées dans les balises suivantes:")
                for tag in vulnerable_tags:
                    print(f"\033[1;31;40m",tag)
            else:
                print("Aucune vulnérabilité XSS détectée.")
        except requests.RequestException as e:
            print("Erreur lors de la requête :", e)

    url = "http://localhost/Vulnerable-Web-Application/XSS/XSS_level1.php"  # CIBLE
    detect_xss(url)
