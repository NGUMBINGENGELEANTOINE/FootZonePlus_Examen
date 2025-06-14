from .models import Match, Place, Reservation, PlaceReservee

def reserver_meilleure_place(utilisateur, match_id, type_place='Standard'):
    match = Match.objects.get(id=match_id)
    place_dispo = Place.objects.filter(match=match, type=type_place, est_disponible=True).order_by('rangée', 'numéro').first()

    if place_dispo:
        reservation = Reservation.objects.create(
            utilisateur = utilisateur,
            match = match,
            total = place_dispo.prix,
            statut = 'confirmée'
        )
        PlaceReservee.objects.create(reservation=reservation, place=place_dispo)
        place_dispo.est_disponible = False
        place_dispo.save()
        return reservation
    else:
        raise Exception("Aucune place disponible")