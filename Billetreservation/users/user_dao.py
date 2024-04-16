import database
from users.user import User
from flask_bcrypt import Bcrypt



class UserDao:
    connexion = database.connect_db()
    cursor = connexion.cursor()


    @classmethod
    def create(cls,user: User):
        sql = "INSERT INTO user (nom_complet,username,password, is_admin) VALUES (%s,%s,%s,%s)"
        params = (user.nom_complet,user.username,user.password, user.is_admin)
        try:
            UserDao.cursor.execute(sql, params)
            UserDao.connexion.commit()
            message = 'success'        
        except Exception as error:
            message = 'failure'
        return message

    @classmethod
    def list_all(cls):
        sql = "SELECT * FROM user"
        try:
            UserDao.cursor.execute(sql)
            users = UserDao.cursor.fetchall()
            message = 'success'
        except Exception as error:
            users = []
            message = 'error'
        return (message, users)
    
    @classmethod
    def get_one(cls,username,password):
        sql = "SELECT * FROM user WHERE username = %s AND password=%s"
        try:
            UserDao.cursor.execute(sql,(username,password))
            user = UserDao.cursor.fetchone()
            message = 'success'
        except Exception as error:
            message = 'failure'
            user =()
            message= user
        return (message, user)
    
    @classmethod
    def get_hashed_password(cls, username, password):
        sql = "SELECT password FROM user WHERE username = %s"
        try:
            UserDao.cursor.execute(sql, (username,))
            hashed_password = UserDao.cursor.fetchone()
            if hashed_password:
                hashed_password = hashed_password[0]
                is_valid = Bcrypt.check_password_hash(hashed_password, password)
                
                if is_valid:    
                    return hashed_password  
                else:
                    message= "Password incorrect"
            else:
                message = "Username not found"
        except Exception as eror:
            print("Error occurred while fetching hashed password")
            message = 'failure'        
        return (message)