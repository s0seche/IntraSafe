from action.option1.scan import nmap_scan_common
from action.option1.scan import nmap_scan_elargie
from action.option1.scan import get_ip_from_json

def option1_main():
    choix = 'y'
    while choix.lower() == 'y' or choix == 'yes':
        json_file_path = 'configuration/conf.json'
        target = get_ip_from_json(json_file_path)
        if target:
            nmap_scan_common(target)
        else:
            print("Erreur lors de la récupération de l'adresse IP à partir du fichier JSON.")    
        
        scan_elargie = str(input("Voulez-vous scanner tout les ports ? (y/n) "))
        if scan_elargie == 'y':
            nmap_scan_elargie(target)
            choix = str(input("Voulez-vous relancer le scan ? (y/n): "))
        else:        
            choix = str(input("Voulez-vous relancer le scan ? (y/n): "))
