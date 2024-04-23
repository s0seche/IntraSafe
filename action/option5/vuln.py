import requests
from bs4 import BeautifulSoup
def jibou():
        
    # Fonction pour détecter les failles XSS
    def detect_xss(url):
        try:
            # Envoie de la requête GET à l'URL spécifiée
            response = requests.get(url)

            # Analyse du contenu HTML
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

    # Exemple d'utilisation
    url = "http://localhost/Vulnerable-Web-Application/XSS/XSS_level1.php"  # Remplacez par l'URL de votre site cible
    detect_xss(url)
