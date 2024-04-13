class User:
    def __init__(self, nom, prenom, vols) -> None:
        self.__nom = nom
        self.__prenom= prenom
        self.__vols= vols
        
        @property
        def nom(self):
            return self.__nom
        
        @nom.setter
        def nom(self, value):
            self.__nom= value

        @property
        def prenom(self):
            return self.__prenom

        @prenom.setter
        def prenom(self, value):
            self.__prenom = value

        @property
        def vols(self):
            return self.__vols

        @vols.setter
        def vols(self, value):
            self.__vols = value
    
