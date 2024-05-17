from shodan import Shodan
import json

def print_pretty_json(data, indent=0):
    for key, value in data.items():
        if isinstance(value, dict):
            print('\t' * indent + f'{key}:')
            print_pretty_json(value, indent + 1)
        elif isinstance(value, list):
            print('\t' * indent + f'{key}:')
            for item in value:
                print('\t' * (indent + 1) + str(item))
        else:
            print('\t' * indent + f'{key}: {value}')

def shodan_scan(json_file_path):
    def get_ip_from_json(json_file_path):
        try:
            with open(json_file_path) as json_file:
                data = json.load(json_file)
                return data.get('IP')
        except Exception as e:
            print(f"Error reading JSON file: {e}")
            return None
    
    try:
        api = Shodan('ThnmcmUTdjqCLCkkT2aHLqP5sLI1QgsO') # Clé API Shodan
        target = get_ip_from_json(json_file_path)

        if target:
            result = api.host(target)
            result_json = json.dumps(result)

            with open('osint.json', 'w') as f:
                f.write(result_json)
            print("Les données ont été enregistrées dans osint_parse.json.")

            def extract_info(json_file):
                with open(json_file, 'r') as f:
                    data = json.load(f)
                
                latitude = data.get('latitude')
                longitude = data.get('longitude')
                isp = data.get('isp')
                org = data.get('org')
                city = data.get('city')
                country_name = data.get('country_name')
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

            output_file = "action/option7/osint_parse.json"
            json_file = "osint.json"
            infos = extract_info(json_file)

            with open(output_file, 'w') as outfile:
                json.dump(infos, outfile, indent=4)

            with open(output_file, 'r') as file:
                data = json.load(file)

            # Afficher les données JSON de manière jolie
            print_pretty_json(data)
        else:
            print("L'adresse IP cible n'a pas été récupérée avec succès.")
    except Exception as e:
        print(f"An error occurred: {e}")
