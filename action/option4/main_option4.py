from action.option4.connectivity import main_bruteforce

def main_option4():
    choix = 'y'
    
    while choix.lower() in ['y', 'yes']:
        print("Tentative de connexion avec les identifiants par défaut")
        main_bruteforce()
        choix = input(str("Voulez vous continuer ? "))  

   