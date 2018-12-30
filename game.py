from map import Map

class Game:

    def __init__(self, numPlayers):
        self.__numPlayers = numPlayers
        self._map = Map()
        self._turn = None
        self._turnOrder = []
    

    def nextTurn(self):
        self._turn = self._turnOrder[self._turnOrder.index(self._turn)+1]