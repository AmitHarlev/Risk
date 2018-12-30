from map import Map
from random import shuffle
from color import Color

class Game:

    def __init__(self, playersArray):
        self.__numPlayers = len(playersArray)
        self.__players = playersArray
        self._map = Map()
        self._turn = None
        self._turnOrder = []

    def assignColors(self):
        availableColors = [Color.RED, Color.BLACK, Color.BLUE, Color.YELLOW, Color.GREEN, Color.ORANGE]
        for index, player in enumerate(self.__players):
            player.color = availableColors[index]

    def handOutTerritories(self):
        territories = self._map.nodes.keys()
        shuffle(territories)
        for index, territory in enumerate(territories):
            val = index % self.__numPlayers
            self.__players[val].territories = self.__players[val].territories.append(territory)

    def nextTurn(self):
        self._turn = self._turnOrder[self._turnOrder.index(self._turn)+1]