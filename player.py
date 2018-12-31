from color import Color
from territory import Territory

class Player:

    def __init__(self, color: Color):
        self.__color = color
        self._troops = 0
        self._territories = []
    
    @property
    def color(self):
        return self.__color

    @property
    def troops(self):
        return self._troops


# THIS FUNCTION NEEDS TO BE CHANGED -- We need to consider all the different times troops are moved to a new territory
    def placeTroops(self, troops: int, territory):
        assert num <= self._troops
        territory.color = self.__color
        territory.addTroops(troops)
        self._troops -= troops

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
        return playerState