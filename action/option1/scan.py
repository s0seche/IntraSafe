import json
import time
import nmap

json_file_path = 'conf.json'
output_file_path = 'action/option1/scan.json'

def get_ip_from_json(json_file_path):
    try:
        with open(json_file_path) as json_file:
            data = json.load(json_file)
            target = data.get('IP')
            return target
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier JSON : {e}")
        return None

def nmap_scan_common(target):
    try:
        print(f"Scan en cours avec pour cible {target}")
        start_time = time.time()

        nm = nmap.PortScanner()
        nm.scan(hosts=target, arguments='-sT -A')  

        scan_results = {
            'scan_time': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            'targets': []
        }

        for host in nm.all_hosts():
            if host != '192.168.1.1':  # Exclusion de l'adresse IP spécifiée
                host_info = {
                    'host': host,
                    'protocols': []
                }
                for proto in nm[host].all_protocols():
                    protocol_info = {
                        'protocol': proto,
                        'ports': []
                    }
                    ports = nm[host][proto].keys()
                    for port in ports:
                        port_info = {
                            'port': port,
                            'state': nm[host][proto][port]['state'],
                            'service': nm[host][proto][port]['name'],
                            'version': nm[host][proto][port]['version']
                        }
                        protocol_info['ports'].append(port_info)
                    host_info['protocols'].append(protocol_info)
                scan_results['targets'].append(host_info)

        end_time = time.time()
        duration = end_time - start_time
        print(f"\nScan terminé en {duration:.2f} secondes.")
        save_scan_results_to_json(scan_results, output_file_path)

    except nmap.PortScannerError as e:
        print(f"Une erreur s'est produite : {e}")

def save_scan_results_to_json(scan_results, output_file_path):
    try:
        if scan_results is None:
            return
        
        filtered_results = []

        for target in scan_results['targets']:
            for protocol in target['protocols']:
                for port_info in protocol['ports']:
                    filtered_result = {
                        'host': target['host'],
                        'port': port_info['port'],
                        'service': port_info['service']
                    }
                    filtered_results.append(filtered_result)

        with open(output_file_path, 'w') as json_file:
            json.dump(filtered_results, json_file, indent=4)

        print(f"Les résultats du scan ont été enregistrés dans {output_file_path}.")
    except Exception as e:
        print(f"Erreur lors de l'enregistrement des résultats du scan : {e}")

def display_scan_results(json_file_path):
    try:
        with open(json_file_path) as json_file:
            data = json.load(json_file)
            print(json.dumps(data, indent=4))
    except FileNotFoundError:
        print(f"Le fichier {json_file_path} n'a pas été trouvé.")
    except Exception as e:
        print(f"Une erreur s'est produite lors de la lecture du fichier JSON : {e}")
