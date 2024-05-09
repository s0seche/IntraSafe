from action.option1.main_option1  import option1_main
from action.option2.main_option2 import option2_main
from action.option3.main_option3 import option3_main
from action.option4.main_option4 import main_option4 
from action.option5.exploit_vuln import option5_main
from action.option5.vuln import jibou
from action.option6.data_detection import option6_main
from action.option7.osint import get_info_ip
from action.option8.generate_pdf import generate_pdf_vulnerability_report

#INIT conf file

def get_choice():
    while True:
        try:
            choice = int(input("\033[1;34;40mEntrez votre choix: "))
            if choice < 1 or choice > 9:
                print("\033[1;31;40mVeuillez entrer un nombre entre 1 et 9.")
                continue
            return choice
        except ValueError:
            continue



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
    print("\033[1;33;40m7.    shodan                    7")    
    print("\033[1;33;40m8. Generate report              8") # auto detectction  
    print("\033[1;33;40m9. Quitter                      9")

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
            get_info_ip("conf.json")
        elif choice == 8:
            generate_pdf_vulnerability_report('action/option1/scan.json', 'report.pdf')
            

                

        elif choice == 9:
            print("\033[1;31;40mAu revoir ;)!")
            break

if __name__ == "__main__":
    main()
