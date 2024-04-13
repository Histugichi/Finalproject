from voyageur import utilisateur
import database
class Userdao:
    connexion = database.connect_db()
    sursor = connexion.cursor()

    @classmethod
    def get_one(cls, prenom, vols):
        sql ="SELECT * FROM user WHERE usernames=%s"
        try:
            Userdao.cursor.execute(sql,(prenom,))
            user= Userdao.cursor.fetchone()
            message= 'success'
        except Exception as error:
           message='failure'
           user=()
        return (user, message)
