from color import Color
from territory import Territory
from card import Deck

class Player:

    def __init__(self, color: Color):
        self.__color = color
        self._troops = 0
        self._territories = []
        self._cards = []
        self._conquer = False
    
    @property
    def color(self):
        return self.__color

    @property
    def troops(self):
        return self._troops

    @property
    def conquer(self):
        return self._conquer

    @conquer.setter
    def conquer(self, conquer: bool):
        self._conquer = conquer

    def addCard(self, card):
        self._cards.append(card)
    
    def getCards(self):
        return self._cards
    
    def removeCard(self, cardTerritory):
        self._cards = [card for card in self._cards if card.territory != cardTerritory]


    # This is for placing troops in a territory (start or just defeated)
    # However it does not remove troops from the player or other territory
    # That must be done seperately
    def placeTroops(self, numTroops: int, territory):
        assert numTroops <= self._troops
        territory.color = self.__color
        territory.addTroops(numTroops)

    def removeTroops(self, numTroops):
        self._troops -= numTroops

    @property
    def territories(self):
        return self._territories

    @troops.setter
    def troops(self, numTroops: int):
        assert self._troops == 0
        self._troops = numTroops

    def addTerritory(self, territory: Territory):
        self._territories.append(territory)

    def removeTerritory(self, territory: Territory):
        self._territories.remove(territory)

    def getPlayerState(self):
        playerState = {}
        playerState["troops"] = self._troops
        playerState["territories"] = self._territories
        playerState["cards"] = self._cards
        return playerState