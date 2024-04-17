import time 
import nmap
import os
import json

json_file_path = '../configuration/conf.json'  # Chemin vers le fichier JSON contenant l'adresse IP à scanner
output_file_path = 'scan.json'  # Chemin pour enregistrer le fichier JSON de sortie

def get_ip_from_json(json_file_path):
    try:
        with open(json_file_path) as json_file:
            data = json.load(json_file)
            target = data.get('IP')
            return target
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return None

def nmap_scan_common(target):
    ip_address = get_ip_from_json(json_file_path)
    print(f"Scan en cours avec pour cible {target}")
    start_time = time.time()

    if ip_address:
        # Scanner l'adresse IP
        nm = nmap.PortScanner()
        try:  
            nm.scan(hosts=ip_address, arguments='-sS -sV')  # Utilisation des options -sS (Scan SYN) et -sV (Détection de version)
            # Affichage des résultats
            scan_results = {}
            for host in nm.all_hosts():
                scan_results[host] = {}
                for proto in nm[host].all_protocols():
                    scan_results[host][proto] = {}
                    ports = nm[host][proto].keys()
                    for port in ports:
                        port_number = int(port)
                        service_name = nm[host][proto][port]['name']
                        service_version = nm[host][proto][port]['version']
                        port_state = nm[host][proto][port]['state']
                        scan_results[host][proto][port_number] = {
                            'state': port_state,
                            'service': service_name,
                            'version': service_version
                        }
            end_time = time.time()
            duration = end_time - start_time
            print(f"\nScan terminé en {duration:.2f} secondes.")
            save_scan_results_to_json(scan_results, output_file_path)
        except nmap.PortScannerError as e:
            print(f"Une erreur s'est produite : {e}")
    else:
        print("Impossible de récupérer l'adresse IP à partir du fichier JSON.")
def save_scan_results_to_json(scan_results, output_file_path):
    try:
        formatted_results = []
        for host, protocols in scan_results.items():
            for proto, ports in protocols.items():
                for port, data in ports.items():
                    formatted_results.append({
                        "host": host,
                        "port": int(port),
                        "service": data["service"],
                        "version": data.get("version", ""),
                        "state": data.get("state", "")
                    })

        with open(output_file_path, 'w') as json_file:
            json.dump(formatted_results, json_file, indent=4)
        print(f"Les résultats du scan ont été enregistrés dans {output_file_path}.")
    except Exception as e:
        print(f"Erreur lors de l'enregistrement des résultats du scan : {e}")

# Appel de la fonction pour scanner
if __name__ == "__main__":
    nmap_scan_common("Your_Target_IP")
