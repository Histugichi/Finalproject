class Reservation:
    def __init__(self,nom,date, statut) -> None:
        self.__nom = nom
        self.__date = date
        self.__statut= statut

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, value):
        self.__nom = value

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, value):
        self.__date = value

    @property
    def statut(self):
        return self.__statut

    @statut.setter
    def statut(self, value):
        self.__statut = value

     

   