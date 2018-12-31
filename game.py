from map import Map
from random import shuffle
from color import Color
from player import Player

class State:
    PREGAME = 1
    INITIALPLACEMENT = 2
    PLAY = 3
    END = 4

class Game:

    def __init__(self, playersArray: {Color:Player}):
        self.__numPlayers = len(playersArray)
        self.__players = playersArray
        self._map = Map()
        self._turn = None
        self._turnOrder = self.assignTurnOrder()
        self._gamePhase = State.PREGAME

    # def assignColors(self):
    #     availableColors = [Color.RED, Color.BLACK, Color.BLUE, Color.YELLOW, Color.GREEN, Color.ORANGE]
    #     for index, player in enumerate(self.__players):
    #         player.color = availableColors[index]

    def assignTurnOrder(self):
        return [Color.RED, Color.BLUE, Color.GREEN, Color.ORANGE]

    def handOutTerritories(self):
        territories = self._map.nodes.keys()
        shuffle(territories)
        for index, territory in enumerate(territories):
            val = index % self.__numPlayers
            self.__players[val].territories = self.__players[val].territories.append(territory)

    def nextTurn(self):
        self._turn = self._turnOrder[(self._turnOrder.index(self._turn)+1) % self.numPlayers]

    def giveTroops(self):
    	for player in self.__players:
    		player.troops =  50 - (self.__numPlayers * 5)

    def initiateTroops(self):
    	for player in self.__players:
    		for territory in player.territories:
    			territory.placeTroops(1, player.color)
    			player.removeTroops(1)
    
    def getGameState(self):
        gameState = {}
        players = {}
        # 
        gameState["players"] = self.__players
        gameState["turn"] = self._turn
        gameState["phase"] = self._gamePhase
        gameState["map"] = self._map.getMapState()
        return gameState



