from map import Map
from random import shuffle
from color import Color
from player import Player
from territory import Territories

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
        self._turnOrder = self.assignTurnOrder()
        self._turn = None
        self._gamePhase = State.PREGAME

    # def assignColors(self):
    #     availableColors = [Color.RED, Color.BLACK, Color.BLUE, Color.YELLOW, Color.GREEN, Color.ORANGE]
    #     for index, player in enumerate(self.__players):
    #         player.color = availableColors[index]

    @property
    def players(self):
        return self.__players

    def assignTurnOrder(self):
        return [Color.RED, Color.BLUE, Color.GREEN, Color.ORANGE]

    def handOutTerritories(self):
        territories = list(self._map.nodes.keys())
        shuffle(territories)
        for index, territory in enumerate(territories):
            val = index % self.__numPlayers
            valColor = list(self.__players.keys())[val]
            self.__players[valColor].territories.append(territory)

    def nextTurn(self):
        self._turn = self._turnOrder[(self._turnOrder.index(self._turn)+1) % self.__numPlayers]
        player  = self.__players[self._turn]
        if (not player.troops and self._gamePhase == State.INITIALPLACEMENT):
            self.nextTurn()

    def initialTroops(self):
    	for player in self.__players.values():
    		player.troops =  50 - (self.__numPlayers * 5)

    def initiateTroops(self):
        for player in self.__players.values():
    	    for territoryEnum in player.territories:
    		    player.placeTroops(1, self._map.nodes[territoryEnum])
    		    player.removeTroops(1)
        self._gamePhase = State.INITIALPLACEMENT
        self._turn = self._turnOrder[0]
    
    def initialPhasePlaceUnit(self, playerColorEnum, territoryName):
        if (self._turn == playerColorEnum and self._gamePhase == State.INITIALPLACEMENT):
            player  = self.__players[playerColorEnum]
            territory = self._map.nodes[territoryName]
            player.placeTroops(1, territory)
            player.removeTroops(1)
            if (all([person.troops == 0 for person in self.__players.values()])):
                self._gamePhase = State.PLAY
            self.nextTurn()

    def giveTroops(self, playerColorEnum):
        if (self._turn == playerColorEnum and self._gamePhase == State.PLAY):
            player = self.__players[playerColorEnum]
            player.troops = (len(player.territories) // 3)
            #have to still add continent bonus ***

    def getGameState(self):
        gameState = {}
        players = {}
        for key, player in self.__players.items():
            players[key] = player.getPlayerState()
        gameState["players"] = players
        gameState["turn"] = self._turn
        gameState["phase"] = self._gamePhase
        gameState["map"] = self._map.getMapState()
        return gameState


