import json

def extraire_infos(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    # Extraire les coordonnées GPS
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    
    # Extraire les informations importantes
    isp = data.get('isp')
    org = data.get('org')
    city = data.get('city')
    country_name = data.get('country_name')
    
    # Extraire l'hostname et le nom DNS
    hostnames = data.get('hostnames', [])
    domains = data.get('domains', [])
    
    return {
        "Coordonnées GPS": (latitude, longitude),
        "Informations importantes": {
            "ISP": isp,
            "Organisation": org,
            "Ville": city,
            "Pays": country_name
        },
        "Hostname": hostnames,
        "Nom DNS": domains
    }

# Utilisation de la fonction
json_file = "osint.json"
infos = extraire_infos(json_file)
print(json.dumps(infos, indent=4))
