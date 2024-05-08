from flask import Flask, render_template, jsonify
import json
app = Flask(__name__)

    # Charger les données initiales depuis le fichier JSON
with open('../action/option1/scan.json', 'r') as fichier_json:
    donnees = json.load(fichier_json)
    
with open('../vulnerabilities.json', 'r') as fichier_cve:
    donnees = json.load(fichier_cve)
    # Récupérer l'IP du premier élément du JSON
ip = donnees[0]["host"]

    # Fonction pour actualiser les données
def actualiser_donnees():
    with open('../action/option1/scan.json', 'r') as fichier_json:
        nouvelles_donnees = json.load(fichier_json)
    return nouvelles_donnees

    # Routes
@app.route('/')
def accueil():
    return render_template('index.html', donnees=donnees, ip=ip)
@app.route('/actualiser')
def actualiser():
    nouvelles_donnees = actualiser_donnees()
    return jsonify(nouvelles_donnees)
@app.route('/tableau')
def tableau():
    return render_template('tableau.html', donnees=donnees, ip=ip)
@app.route('/graphique')

def graphique():
    return render_template('graphique.html', donnees=donnees, ip=ip)

@app.route('/tableau-cve')
def tableau_cve():
    return render_template('tableau-cve.html', donnees=donnees, ip=ip)

if __name__ == '__main__':
        app.run(debug=False)

