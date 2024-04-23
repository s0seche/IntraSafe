from action.option1.main_option1 import option1_main
from action.option2.main_option2 import option2_main
from action.option3.main_option3 import option3_main
from action.option4.main_option4 import main_option4 
from action.option5.exploit_vuln import option5_main
from action.option5.vuln import jibou
from action.option6.data_detection import option6_main
from action.option7.reporting import main_option7
from configuration.conf import lire_informations, creer_fichier, fichier_texte, chemin_fichier_json

#INIT conf file
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
    print("\033[1;33;40m1. Port scanning & services     1")
    print("\033[1;33;40m2. CVE detection                2")
    print("\033[1;33;40m3. Password security            3")
    print("\033[1;33;40m4. Try defaults credentials     4") # add for ftp 
    print("\033[1;33;40m5. Analyze Web site             5") # detect XSS
    print("\033[1;33;40m6. Create personalize wordlist  6") # Cupp 
    print("\033[1;33;40m7.    OSINT TOOl                7")    
    print("\033[1;33;40m8. Pentest                      8") # auto detectction  
    print("\033[1;33;40m9. Quitter                      9")
    print("\033[1;32;40m**********************************************")

def get_choice():
    while True:
        try:
            choice = int(input("\033[1;36;40mChoisissez une option (1-8): "))
            if 1 <= choice <= 9:
                return choice
            else:
                print("\033[1;31;40mVeuillez entrer un nombre entre 1 et 8.")
        except ValueError:
            print("\033[1;31;40mVeuillez entrer un nombre valide.")

def main():
    while True:
        print_logo()
        print_menu()
        choice = get_choice()

        if choice == 1:
            print("\033[1;34;40mVous avez choisi l'option 1.")
            option1_main()
        elif choice == 2:
            print("\033[1;34;40mVous avez choisi l'option 2.")
            option2_main()
        elif choice == 3:
            print("\033[1;34;40mVous avez choisi l'option 3.")
            option3_main()
        elif choice == 4:
            print("\033[1;34;40mVous avez choisi l'option 4.")
            main_option4()
        elif choice == 5:
            print("\033[1;34;40mVous avez choisi l'option 5.")
            jibou()
        elif choice == 6:
            print("\033[1;34;40mVous avez choisi l'option 6.")
            option6_main()
        elif choice == 7:
            print("\033[1;34;40mVous avez choisi l'option 7.")
            main_option7()
        elif choice == 8:
            choix = 'y'
            while choix =='y':
                print("Un pentest va être excuté avec l'ensemble des fonctions de cette toolbox. \nAttention cela ne vous dispense pas d'un réel pentest par des professionels ")
                choix = input(str("Voulez vous re faire le pentest ?"))
                
            """
            option1_main() nmap
            option2_main() search sploit
            option4_main() ping ?
            option5_main() exploit vuln
            main_option7()  rapport
            """
        elif choice == 9:
            print("\033[1;31;40mAu revoir ;)!")
            break

if __name__ == "__main__":
    main()
