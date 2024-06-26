from action.option1.scan import get_ip_from_json, nmap_scan_common, save_scan_results_to_json,display_scan_results
output_file_path = 'scan.json'  # Chemin pour enregistrer le fichier JSON de sortie

def option1_main():
    choix = 'y'
    while choix.lower() in ['y', 'yes']:
        json_file_path = 'conf.json'
        target = get_ip_from_json(json_file_path)
        if target:
            results_common = nmap_scan_common(target)
            display_scan_results("action/option1/scan.json")
        else:
            print("Erreur lors de la récupération de l'adresse IP à partir du fichier JSON.")
            return
        
        choix = input("Voulez-vous relancer le scan ? (y/n): ")

    # Sauvegarder les résultats à la fin de la boucle
    save_scan_results_to_json(results_common, output_file_path)  # Ajouter output_file_path comme argument
