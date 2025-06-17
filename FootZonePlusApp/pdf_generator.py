import os
import qrcode
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from django.conf import settings

def generer_billet_pdf(reservation):
    billet_dir = os.path.join(settings.MEDIA_ROOT, 'billets')
    os.makedirs(billet_dir, exist_ok=True)

    filename = f"billet_{reservation.id}.pdf"
    filepath = os.path.join(billet_dir, filename)

    # QR Code
    qr_data = f"Réservation ID: {reservation.id} - Utilisateur: {reservation.utilisateur.username}"
    qr = qrcode.make(qr_data)
    qr_path = os.path.join(billet_dir, f"qr_{reservation.id}.png")
    qr.save(qr_path)

    # Génération PDF
    c = canvas.Canvas(filepath, pagesize=A4)
    c.drawString(100, 800, f"Billet pour {reservation.utilisateur.username}")
    c.drawString(100, 780, f"Match : {reservation.match.equipe_locale} vs {reservation.match.equipe_visiteuse}")
    c.drawString(100, 760, f"Date : {reservation.match.date_heure.strftime('%Y-%m-%d %H:%M')}")
    place = reservation.places.first().place
    c.drawString(100, 740, f"Place : Rangée {place.rangée}, Numéro {place.numero}, Type {place.type}")
    c.drawImage(qr_path, 100, 600, width=100, height=100)
    c.save()

    # Stocke le chemin dans pdf_file
    relative_path = f'billets/{filename}'
    reservation.pdf_file.name = relative_path
    reservation.save()
