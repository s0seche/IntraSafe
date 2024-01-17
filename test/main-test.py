# clean version ??
# A valider

from action.option1.scan import option1_main
from action.option2.vuln_detection import option2_main
from action.option3.pwd_secure import option3_main
from action.option4.connectivity import option4_main
from action.option5.exploit_vuln import option5_main
from action.option6.data_detection import option6_main
from action.option7.reporting import option7_main
from configuration.conf import lire_informations, creer_fichier, fichier_texte, chemin_fichier_json

def init_configuration():
    informations = lire_informations(fichier_texte)
    creer_fichier(informations, chemin_fichier_json)

def print_logo():
    print("\033[1;35;40m")
    print(" /$$$$$$             /$$                         /$$$$$$$             /$$$$$$ ")
    print("|_  $$_/            | $$                        | $$__  $$           /$$__  $$")
    print("  | $$   /$$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$ | $$  \ $$  /$$$$$$ | $$  \\__/")
    print("  | $$  | $$__  $$|_  $$_/   /$$__  $$ |____  $$| $$  | $$ /$$__  $$| $$$$   ")
    print("  | $$  | $$  \ $$  | $$    | $$  \__/  /$$$$$$$| $$  | $$| $$$$$$$$| $$_/   ")
    print("  | $$  | $$  | $$  | $$ /$$| $$       /$$__  $$| $$  | $$| $$_____/| $$     ")
    print(" /$$$$$$| $$  | $$  |  $$$$/| $$      |  $$$$$$$| $$$$$$$/|  $$$$$$$| $$     ")
    print("|______/|__/  |__/   \___/  |__/       \_______/|_______/  \_______/|__/     ")
    print("                                                                               ")
    print("                                                                               ")


def print_menu():
    print("\033[1;32;40m**********************************************")
    print("***               Automate                 ***")
    print("***           Your penetration tests       ***")
    print("***               IntraDef                 ***")
    print("**********************************************")
    options = [
        "Port scanning & services",
        "Vulnerability detection",
        "Password security",
        "Try connectivity",
        "Exploit Vulnerability",
        "Sensitive data detection",
        "Reporting",
        "Quitter"
    ]
    for i, option in enumerate(options, start=1):
        print(f"\033[1;33;40m{i}. {option}")

def get_choice():
    while True:
        try:
            choice = int(input("\033[1;36;40mChoisissez une option (1-8): "))
            if 1 <= choice <= 8:
                return choice
            else:
                print("\033[1;31;40mVeuillez entrer un nombre entre 1 et 8.")
        except ValueError:
            print("\033[1;31;40mVeuillez entrer un nombre valide.")

def execute_option(choice):
    options = [
        option1_main,
        option2_main,
        option3_main,
        option4_main,
        option5_main,
        option6_main,
        option7_main,
        None  
    ]
    if choice == 8:
        print("\033[1;31;40mAu revoir ;)!")
        return False
    elif options[choice - 1] is not None:
        options[choice - 1]()
    return True

def main():
    init_configuration()
    
    while True:
        print_logo()
        print_menu()
        choice = get_choice()
        continue_program = execute_option(choice)
        
        if not continue_program:
            break

if __name__ == "__main__":
    main()
