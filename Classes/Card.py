class Card:
    def __init__(self):
        self.__cardName = None
        self.__cardType = None
        self.__cardColor = None
        self.__cardStatus = None
        self.__cardLocation = None
        self.__cardImage = None

    # =============getter method=================#
    def get_cardName(self):
        return self.__cardName

    def get_cardType(self):
        return self.__cardType

    def get_cardColor(self):
        return self.__cardColor

    def get_cardStatus(self):
        return self.__cardStatus

    def get_CardLocation(self):
        return self.__cardLocation

    def get_cardImage(self):
        return self.__cardImage

    # =================setter method================#
    def set_cardName(self, cardName):
        self.__cardName = cardName

    def set_cardType(self, cardType):
        self.__cardType = cardType

    def set_cardColor(self, cardColor):
        self.__cardColor = cardColor

    def set_cardStatus(self, cardStatus):
        self.__cardStatus = cardStatus

    def set_cardLocation(self, cardLocation):
        self.__cardLocation = cardLocation

    def set_cardImage(self, cardImage):
        self.__cardImage = cardImage
