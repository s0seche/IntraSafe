from action.option1.scan import nmap_scan
from action.option1.scan import get_ip_from_json

def option1_main():
    choix = 'y'
    while choix.lower() == 'y' or choix == 'yes':
        
        target_ip = get_ip_from_json('conf.json')
        if target_ip:
            nmap_scan(target_ip)
        else:
            print("Erreur lors de la récupération de l'adresse IP à partir du fichier JSON.")    
        
        choix = str(input("Voulez-vous relancer le scan ? (y/n): "))