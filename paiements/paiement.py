class Paiement:
    def __init__(self,montant,mode_paiement,id_paiement,date,CVV) -> None:
        
        self.__montant = montant
        self.__mode_paiement = mode_paiement
        self.__id_paiement = id_paiement
        self.__date = date
        self.__CVV = CVV

    @property
    def montant(self):
        return self.__montant

    @montant.setter
    def montant(self, value):
        self.__montant = value

    @property
    def mode_paiement(self):
        return self.__mode_paiement

    @mode_paiement.setter
    def mode_paiement(self, value):
        self.__mode_paiement = value

    @property
    def id_paiement(self):
        return self.__id_paiement

    @id_paiement.setter
    def id_paiement(self, value):
        self.__id_paiement = value

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, value):
        self.__date = value

    @property
    def CVV(self):
        return self.__CVV

    @CVV.setter
    def CVV(self, value):
        self.__CVV = value

        