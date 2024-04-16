import database
from reservations.statut import ReservationStatut
from reservations.reservation import Reservation
from flask_bcrypt import Bcrypt


class ReservationDao:
    connexion = database.connect_db()
    cursor = connexion.cursor()

    def __init__(self) -> None:
        pass

    @classmethod
    def reserver_place(cls, nom, date, statut):
        sql = "INSERT INTO reservations (nom, prenom, place, place_speciale) VALUES (%s,%s, %s, 0)"
        params = (nom, date, statut)   
        try:
            ReservationDao.cursor.execute(sql, params)
            ReservationDao.connexion.commit()    
            print(f"{nom} a réservé une place.")          
        except Exception as error:
            return f"Erreur lors de la reservation: {error}"
        
        
    @classmethod
    def places_reservees(cls):
        sql = "SELECT SUM(place) FROM reservations"
        try:
            ReservationDao.cursor.execute(sql)
            nombre_reservations = ReservationDao.cursor.fetchone()[0]
            print (f"Nombre de reservations: {nombre_reservations}")
            return nombre_reservations   
        except Exception as error:
            print (f"Erreur lors de la récupération des réservations! {error}")
            return 0

       
    @classmethod
    def nombre_places_disponibles(cls):
        capacite_totale= 200
        try:
            reservations= ReservationDao.places_reservees()
            disponibles = capacite_totale - reservations
            return disponibles if disponibles >= 0 else 0          
        except Exception as error:
            print(f"Erreur lors du calcul des places disponibles!", error)
            return 0

    @classmethod
    def filtrer_reservations_par_personne(cls,nom):
        sql = """SELECT *FROM reservations WHERE nom = %s"""
        try:
            ReservationDao.cursor.execute(sql,(nom,))
            reservations = ReservationDao.cursor.fetchall()
            if reservations:
                return reservations, f"La personne {nom} a réservé la place."
            else:
                return None, f" Malheureusement, aucune reservation à été fait pour {nom}!"
        except Exception as error:
           return None, f"Erreur lors de la récupération des réservations : {error}"
        

    @classmethod
    def annuler_reservation(cls,nom):
        sql = """DELETE FROM reservations WHERE nom = %s"""
        try:
            ReservationDao.cursor.execute(sql, (nom,))
            ReservationDao.connexion.commit()
            if ReservationDao.cursor.rowcount > 0:
                return f"La réservation au nom {nom} a bien été annulée."
            else:
                return f"Impossible d'annuler cette réservation car elle n'existe pas."
        except Exception as error:
            return f"Une erreur est survenue lors de l'annulation de la réservation : {error}"
           
                