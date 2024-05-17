from flask import Flask, render_template, jsonify
import json
app = Flask(__name__)

with open('../conf.json', 'r') as ip_title:
    data = json.load(ip_title)
    ip = data["IP"]


with open('../action/option1/scan.json', 'r') as fichier_json:
    donnees = json.load(fichier_json)

with open('../vulnerabilities.json', 'r') as fichier_cve:
    donnees_cve = json.load(fichier_cve)

    # Fonction pour actualiser les PORTS
def actualiser_donnees():
    with open('../action/option1/scan.json', 'r') as fichier_json:
        nouvelles_donnees = json.load(fichier_json)
    return nouvelles_donnees

    # Fonction pour actualiser les CVEs
def actualiser_donnees_cve():
    with open('../vulnerabilities.json', 'r') as fichier_json_cve:
        nouvelles_cve = json.load(fichier_json_cve)
    return nouvelles_cve


    # Routes
@app.route('/')
def accueil():
    return render_template('index.html', donnees=donnees, ip=ip)

@app.route('/actualiser')

def actualiser():
    nouvelles_donnees = actualiser_donnees()
    return jsonify(nouvelles_donnees)


@app.route('/actualiser_cve')
def actualiser_cve():
    nouvelles_cve = actualiser_donnees_cve()  
    return jsonify(nouvelles_cve)



@app.route('/tableau')
def tableau():
    return render_template('tableau.html', donnees=donnees, ip=ip)
@app.route('/graphique')

def graphique():
    return render_template('graphique.html', donnees=donnees, ip=ip)

@app.route('/tableau-cve')
def tableau_cve():
    return render_template('tableau_cve.html', donnees=donnees, ip=ip)

if __name__ == '__main__':
        app.run(debug=False)

