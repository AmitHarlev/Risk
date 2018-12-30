from map import Map
from random import shuffle

class Game:

    def __init__(self, playersArray):
        self.__numPlayers = len(playersArray)
        self.__players = playersArray
        self._map = Map()
        self._turn = None
        self._turnOrder = []
        self.handOutTerritories()


    def handOutTerritories(self):
        territories = self._map.nodes.keys()
        shuffle(territories)
        for index, territory in enumerate(territories):
            val = index % self.__numPlayers
            self.__players[val].territories = self.__players[val].territories.append(territory)

    def nextTurn(self):
        self._turn = self._turnOrder[self._turnOrder.index(self._turn)+1]