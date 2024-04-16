class User:
    def __init__(self,nom_complet, username, password, is_admin) -> None:
        self.__nom_complet = nom_complet
        self.__username = username
        self.__password = password
        self.__is_admin = is_admin

    @property
    def nom_complet(self):
        return self.__nom_complet

    @nom_complet.setter
    def nom_complet(self, value):
        self.__nom_complet = value

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value

    @property
    def is_admin(self):
        return self.__is_admin

    @is_admin.setter
    def is_admin(self, value):
        self.__is_admin = value


   

    

        

  

    
    
