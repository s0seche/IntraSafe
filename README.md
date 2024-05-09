# IntraSafe: Boîte à outils pour l'automatisation des tests de sécurité 🛡️

## Projet de fin d'année - Master 1 🎓

Bienvenue dans IntraSafe, un projet toolbox dans le cadre du projet de fin d'année du Master 
L' objectif principal de cette boîte à outils est d'automatiser les tests de sécurité, facilitant ainsi la détection de vulnérabilités et la sécurisation des systèmes.

## Fonctionnalités

1. **Découverte de ports et de services** 🌐
   - Identifiez les ports ouverts et les services en cours d'exécution sur un système.

2. **Détection de vulnérabilités** 🚨
    - Identifiez les failles de sécurité existantes 
    
3. **Analyse de la sécurité des mots de passe fournis** 🔐
   - Évaluez la robustesse des mots de passe fournis pour renforcer la sécurité. 
        - A partir de données sur excel ou keepass

4. **Tests des identifiants  d'authentification par défaut** 🤖
   - Effectuez des tests d'authentification pour évaluer la résistance de votre service SSH.

5. **Détection de vulnérabilités Web** 💻
   - Détecter les vulnérabtilité XSS sur page web .
        - La faille XSS (Cross-Site Scripting) est une vulnérabilité de sécurité sur les sites web, permettant aux attaquants d'injecter et d'exécuter du code malveillant dans les navigateurs des utilisateurs.

6. **Création de Wordlist** 🕵️‍♂️
   - Crée votre propre wordlist personalisé pour vos attaques.

7. **Génerer un scan Shodanb** 📊
   - Générez des rapports détaillés sur une adresse IP

8. **Création de rapports et visualisations graphiques** 📊
   - Générez des rapports détaillés sur les failles trouvées pour faciliter la compréhension des résultats.

## Configuration

```bash
git clone https://github.com/s0seche/IntraSafe.git
```
```bash
pip install -r requirements.txt
```

`Avant de commencer`, veuillez insérer vos informations de configuration dans le fichier "conf.json". Cela améliorera votre experience utilisateur de IntraSafe. Il est important de lançer le script avec les droits administrateurs.

```bash
sudo python3 main.py
```
Pour lancer la version Web il faut vous rendre dans le répertoire " flask_appli" et éxucter la comande
```bash
sudo python3 app.py
```

