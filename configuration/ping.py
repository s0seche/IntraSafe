import subprocess
from action.option1.scan import get_ip_from_json

json_file_path = 'configuration/conf.json'
get_ip_from_json(json_file_path)



def ping(host):
    try:
        result = subprocess.run(['ping', '-c', '4', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)

        if "0% packet loss" in result.stdout or "25% packet loss":
            return True
        else:
            return False
    except subprocess.CalledProcessError:
        return False

# Exemple d'utilisation
if ping(target):
    print(f"Ping réussi vers {target}")
else:
    print(f"Échec du ping vers {target}")

