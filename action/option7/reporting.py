from action.option7.web_page import web_application
import webbrowser

def main_option7():
    choix = 'y'
    while choix.lower() =='y' or choix.lower() =='yes':
            try:
                print(f"Lancement de l'appliaction web...")
                web_application()
                webbrowser.open('http://127.0.0.1:5000/')
                print(f"L'application à finis de s'init \n vous pouvez y accèder à partir \n http://localhost:5000")
            except Exception as e:
                print(f"Erreur lors de l'éxcution de l'application web {e}")
    
    