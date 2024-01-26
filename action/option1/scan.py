import time
import nmap
import json
def get_ip_from_json(json_file_path):
    try:
        with open(json_file_path) as json_file:
            data = json.load(json_file)
            target = data.get('IP')
            return target
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return None


def nmap_scan(target):
    # Récupérer l'adresse IP à partir du fichier JSON
    json_file_path = 'configuration/conf.json'
    ip_address = get_ip_from_json(json_file_path)
    print(f"Scan en cours ...")
    start_time = time.time()

    if ip_address:

        # Scanner l'adresse IP
        nm = nmap.PortScanner()
        try:
            # Utilisation de la méthode scan avec les options spécifiées
            nm.scan(hosts=ip_address, arguments='-A -sT')

            # Affichage des résultats
            for host in nm.all_hosts():
                print(f"Host: {host}")
                for proto in nm[host].all_protocols():
                    print(f"Protocol: {proto}")
                    ports = nm[host][proto].keys()
                    for port in ports:
                        print(f"Port: {port} - State: {nm[host][proto][port]['state']} - Service: {nm[host][proto][port]['name']} - Version: {nm[host][proto][port]['version']}")

            # Indication du temps de fin du scan
            end_time = time.time()
            duration = end_time - start_time
            print(f"\nScan terminé en {duration:.2f} secondes.")
        except nmap.PortScannerError as e:
            print(f"Une erreur s'est produite : {e}")
    else:
        print("Impossible de récupérer l'adresse IP à partir du fichier JSON.")
