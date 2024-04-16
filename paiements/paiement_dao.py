import database
from paiements.paiement import Paiement
from flask_bcrypt import Bcrypt

class PaiementDao:
    connexion = database.connect_db()
    cursor = connexion.cursor()


    @classmethod
    def get_all(cls):
        sql = "SELECT *from paiement"
        try:
            PaiementDao.cursor.execute(sql)
            paiements = PaiementDao.cursor.fetchall()
            message = 'success'
        except Exception as error:
            users = []
            message = 'error'
        return (message, paiements)


    @classmethod
    def ajouter_paiement(cls, montant,mode_paiement,id_paiement,date,CVV):
        sql = "INSERT INTO paiement (montant,mode_paiement,id_paiement,date,CVV) VALUES %s,%s,%s,%s,%s)"
        params = (montant,mode_paiement,id_paiement,date,CVV)
        try:
            PaiementDao.cursor.execute(sql, params)
            PaiementDao.connexion.commit()
            message = 'Paiement ajouté avec succès.'
        except Exception as error:
            message = 'failure to add paiement'
        return message

    @classmethod
    def modifier_paiement(cls, id_paiement, nouveau_paiement):
        sql = "UPDATE paiement SET montant,mode_paiement,id_paiement,date,CVV WHERE 1"
        try:
            PaiementDao.cursor.execute(sql, (nouveau_paiement.attribut1, nouveau_paiement.attribut2, ..., id_paiement))
            PaiementDao.connexion.commit()   
            message = "Le paiement a été modifié avec succès."       
        except Exception as error:
            message= "Erreur lors de la modification du paiement"
        return message


    @classmethod
    def supprimer_paiement(cls, id_paiement):
        sql= "DELETE FROM paiement WHERE id = %s"
        try:
            PaiementDao.cursor.execute(sql,(id_paiement,))
            PaiementDao.connexion.commit()
            message='Le paiement a été supprimé.'
        except Exception as error:
            message= "Erreur lors de la suppression du paiement"
        return message
    
    
    @classmethod
    def recuperer_paiement_par_id(cls, id_paiement):
        sql = "SELECT * FROM paiement WHERE id = %s", (id_paiement,)
        try:
            PaiementDao.cursor.execute(sql,(id_paiement,))
            paiement = PaiementDao.cursor.fetchone()
            if paiement:
                return Paiement(*paiement)
        except Exception as error:
            print("Erreur lors de la récupération du paiement par ID")
        return None
       
    
   