from shodan import Shodan
import json

def get_info_ip(json_file_path):
    print(json_file_path)
    def get_ip_from_json(json_file_path):
        try:
            with open(json_file_path) as json_file:
                data = json.load(json_file)
                return data.get('IP')
        except Exception as e:
            print(f"Error reading JSON file: {e}")
            return None
    
    try:
        api = Shodan('ThnmcmUTdjqCLCkkT2aHLqP5sLI1QgsO')
        target = get_ip_from_json(json_file_path)

        if target:
            result = api.host(target)
            result_json = json.dumps(result)

            with open('osint.json', 'w') as f:
                f.write(result_json)
            print("Les données ont été enregistrées dans osint.json.")

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
            json_file = "action/option7/osint.json"
            infos = extract_info(json_file)

            with open(output_file, 'w') as outfile:
                json.dump(infos, outfile, indent=4)

            print(f"Données écrites dans le fichier : {output_file}")
        else:
            print("L'adresse IP cible n'a pas été récupérée avec succès.")
    except Exception as e:
        print(f"An error occurred: {e}")

