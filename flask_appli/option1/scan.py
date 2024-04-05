import time
import nmap
import json
# Erreur : permision root demandé pour scan udp .. (-sU) 
output_file_path = 'configuration/scan.json'
json_file_path = 'configuration/conf.json'

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
            nm.scan(hosts=ip_address, arguments='-sT -A')  
            # Affichage des résultats
            for host in nm.all_hosts():
                print(f"Host: {host}")
                for proto in nm[host].all_protocols():
                    print(f"Protocol: {proto}")
                    ports = nm[host][proto].keys()
                    for port in ports:
                        print(f"Port: {port} - State: {nm[host][proto][port]['state']} - Service: {nm[host][proto][port]['name']} - Version: {nm[host][proto][port]['version']}")
                        
            end_time = time.time()
            duration = end_time - start_time
            print(f"\nScan terminé en {duration:.2f} secondes.")
        except nmap.PortScannerError as e:
            print(f"Une erreur s'est produite : {e}")
    else:
        print("Impossible de récupérer l'adresse IP à partir du fichier JSON.")
        

def nmap_scan_elargie(target): 
    ip_address = get_ip_from_json(json_file_path)
    print(f"Attention ce type de  scan peut être plus long")
    print(f"Scan en cours avec pour cible {target}")
    start_time = time.time()

    if ip_address:
        # Scanner l'adresse IP
        nm = nmap.PortScanner()
        try:
            nm.scan(hosts=ip_address, arguments='-sT -A -p-')
            # Affichage des résultats
            for host in nm.all_hosts():
                print(f"Host: {host}")
                for proto in nm[host].all_protocols():
                    print(f"Protocol: {proto}")
                    ports = nm[host][proto].keys()
                    for port in ports:
                        print(f"Port: {port} - State: {nm[host][proto][port]['state']} - Service: {nm[host][proto][port]['name']} - Version: {nm[host][proto][port]['version']}")

           
            end_time = time.time()
            duration = end_time - start_time
            print(f"\nScan terminé en {duration:.2f} secondes.")
        except nmap.PortScannerError as e:
            print(f"Une erreur s'est produite : {e}")
    else:
        print("Impossible de récupérer l'adresse IP à partir du fichier JSON.")
