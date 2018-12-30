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

    def removeTroops(self, num):
        assert num <= self._troops
        self._troops -= num

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