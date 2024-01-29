# web_app.py
from flask import Flask, render_template
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import json

def web_application():
    app = Flask(__name__)
    
    def get_ip_from_json(json_file_path):
        try:
            with open(json_file_path) as json_file:
                data = json.load(json_file)
                target = data.get('IP')
                return target
        except Exception as e:
            print(f"Error reading JSON file: {e}")
            return None

    # Route pour la page d'accueil
    @app.route('/')
    def index():
        json_file_path = 'configuration/conf.json'
        ip_address = get_ip_from_json(json_file_path)
        # Générer des valeurs fictives pour les données du diagramme à barres
        x_bar = ["ftp","ssh","smb"]
        y_bar = [10, 12, 16]

        # Création d'un diagramme à barres
        fig_bar = plt.figure(figsize=(8, 4))
        plt.bar(x_bar, y_bar)
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.title('Port découvert')
        
        # Conversion du diagramme à barres en image
        img_bar = BytesIO()
        fig_bar.savefig(img_bar, format='png')
        img_bar.seek(0)
        plot_url_bar = base64.b64encode(img_bar.getvalue()).decode()

        #CAMEMBERT
        labels_pie = ['SQLI', 'XSS', 'DOS', 'RCE']
        sizes_pie = [25, 20, 15, 30]

        fig_pie = plt.figure(figsize=(8, 4))
        plt.pie(sizes_pie, labels=labels_pie, autopct='%1.1f%%', startangle=90)
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.title('Vuln détéctée')

        # Conversion du diagramme en camembert en image
        img_pie = BytesIO()
        fig_pie.savefig(img_pie, format='png')
        img_pie.seek(0)
        plot_url_pie = base64.b64encode(img_pie.getvalue()).decode()

        # Affichage de la page avec les deux diagrammes
        return render_template('index.html', plot_url_bar=plot_url_bar, plot_url_pie=plot_url_pie, ip_address=ip_address)
    app.run(debug=True)  # A RETIRER avant mise en prod !!
