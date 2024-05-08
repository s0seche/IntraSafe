from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import styles
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph
from vulners import VulnersApi
import json

# Définir votre clé API
api_key = "GAMNRV2MFM5JVEQPXWPRBU83HPKXR0RV6YTY38NFCWNSZHR0AMX2CC6DLFUB4ADQ"

# Initialiser l'objet VulnersApi avec votre clé API
vulners_api = VulnersApi(api_key)

# Définir un style pour le texte en gras
styles = getSampleStyleSheet()
bold_style = ParagraphStyle(name='Bold', parent=styles['Normal'])
bold_style.fontName = 'Helvetica-Bold'

def generate_pdf_vulnerability_report(json_file, pdf_file):
    try:
        # Créer un nouveau fichier PDF
        c = canvas.Canvas(pdf_file, pagesize=letter)
        c.setFont("Helvetica", 12)

        # Titre "Intradef" en gras
        c.setFont("Helvetica-Bold", 24)
        title_text = "Intradef"
        title_width = c.stringWidth(title_text)
        c.drawString((letter[0] - title_width) / 2, 750, title_text)

        # En-tête "Jean Baptiste BEL"
        c.setFont("Helvetica", 12)
        header_text = "Jean Baptiste BEL"
        header_width = c.stringWidth(header_text)
        c.drawString((letter[0] - header_width) / 2, 730, header_text)

        with open(json_file, 'r') as file:
            services = json.load(file)

        y_position = 700  # Position verticale initiale après le titre

        for service in services:
            service_name = service["service"]
            port_number = service["port"]  # Ajout du numéro de port

            # Si la section actuelle dépasse la limite de la page, ajouter un saut de page
            if y_position < 100:
                c.showPage()
                c.setFont("Helvetica", 12)
                y_position = 750  # Réinitialiser la position verticale après le saut de page

            # Mettre en gras le nom du service et le numéro de port
            c.saveState()
            c.setFont("Helvetica-Bold", 12)
            c.drawString(50, y_position, "Vulnérabilités pour le service: {} (Port {})".format(service_name, port_number))
            c.restoreState()
            c.drawString(50, y_position - 20, "-" * 70)

            # Récupérer les vulnérabilités pour ce service
            vulnerabilities = vulners_api.find(service_name, limit=3)  # Limitez à 3 vulnérabilités pour chaque service

            # Afficher les vulnérabilités
            y_position -= 40  # Ajustement de l'espacement
            for vulnerability in vulnerabilities:
                c.drawString(50, y_position, "CVE ID: {}".format(vulnerability.get("id")))
                description = vulnerability.get("description")
                if description:
                    c.drawString(50, y_position - 15, "Description: {}".format(description))
                else:
                    c.drawString(50, y_position - 15, "Description: Description non disponible")
                c.drawString(50, y_position - 30, "CVSS Score: {}".format(vulnerability.get("cvss").get("score")))
                references = ", ".join(vulnerability.get("references", []))
                c.drawString(50, y_position - 45, "References: {}".format(references))
                c.drawString(50, y_position - 60, "-" * 70)
                y_position -= 80  # Ajustement de l'espacement

            # Ajuster la position verticale pour le prochain service
            y_position -= 20

        c.save()
        print("Le rapport des vulnérabilités a été généré avec succès dans le fichier PDF:", pdf_file)

    except Exception as e:
        print("Une erreur s'est produite lors de la génération du rapport des vulnérabilités:", e)

# Appel de la fonction pour générer le rapport des vulnérabilités au format PDF
