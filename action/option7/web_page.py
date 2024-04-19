
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
        x_bar = ["bb","ssh","smb"]
        y_bar = [3, 12, 16]

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
"""
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
        x_bar = ["aaa", "ssh", "smb"]
        y_bar = [1, 12, 16]

        # Création d'un diagramme à barres
        fig_bar, ax_bar = plt.subplots(figsize=(8, 4))
        ax_bar.bar(x_bar, y_bar)
        ax_bar.set_xlabel('X-axis')
        ax_bar.set_ylabel('Y-axis')
        ax_bar.set_title('Port découvert')
        
        # Conversion du diagramme à barres en HTML
        html_bar = fig_to_html(fig_bar)

        # CAMEMBERT
        labels_pie = ['SQLI', 'XSS', 'DOS', 'RCE']
        sizes_pie = [25, 20, 15, 30]

        # Création du diagramme en camembert
        fig_pie, ax_pie = plt.subplots(figsize=(8, 4))
        ax_pie.pie(sizes_pie, labels=labels_pie, autopct='%1.1f%%', startangle=90)
        ax_pie.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        ax_pie.set_title('Vuln détéctée')

        # Conversion du diagramme en camembert en HTML
        html_pie = fig_to_html(fig_pie)

        # Affichage de la page avec les deux diagrammes
        return render_template('index.html', html_bar=html_bar, html_pie=html_pie, ip_address=ip_address)

    def fig_to_html(fig):
        img = BytesIO()
        fig.savefig(img, format='png', bbox_inches='tight')
        img.seek(0)
        encoded_img = base64.b64encode(img.getvalue()).decode()
        return f'<img src="data:image/png;base64,{encoded_img}" alt="Graphique">'

    app.run(debug=False)  # A RETIRER avant mise en prod !!
"""