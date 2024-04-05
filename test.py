#Pas sûr de l'utilité. Barre de chargement pour init tous les fichiers.
# A voir avec le temps...

import os
import time
import progressbar

from pouet.option1.scan import option1_main
from pouet.option2.vuln_detection import option2_main
from pouet.option3.pwd_secure import option3_main
from pouet.option4.connectivity import option4_main
from pouet.option5.exploit_vuln import option5_main
from pouet.option6.data_detection import option6_main
from pouet.option7.reporting import option7_main

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
    print("\033[1;33;40m2. Vulnerability detection      2")
    print("\033[1;33;40m3. Password security            3")
    print("\033[1;33;40m4. Try connectivity             4")
    print("\033[1;33;40m5. Exploit Vulnerability        5")
    print("\033[1;33;40m6. Sensitive data detection     6")
    print("\033[1;33;40m7. Reporting                    7")
    print("\033[1;33;40m8. Quitter                      8")
    print("\033[1;32;40m**********************************************")

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

def loading_bar():
    widgets = [
        ' [', progressbar.Percentage(), '] ',
        progressbar.Bar(marker='=', left='[', right=']'),
    ]
    bar = progressbar.ProgressBar(widgets=widgets, max_value=50).start()

    for i in range(30):
        time.sleep(0.1)
        bar.update(i + 1)

    bar.finish()

def main():
    loading_bar()
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
            option4_main()
        elif choice == 5:
            print("\033[1;34;40mVous avez choisi l'option 5.")
            option5_main()
        elif choice == 6:
            print("\033[1;34;40mVous avez choisi l'option 6.")
            option6_main()
        elif choice == 7:
            print("\033[1;34;40mVous avez choisi l'option 7.")
            option7_main
        elif choice == 8:
            print("\033[1;31;40mAu revoir ;)!")
            break

if __name__ == "__main__":
    main()
