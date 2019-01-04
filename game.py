from riskMap import Map, Continent, Continents
from random import shuffle
from color import Color
from player import Player
from territory import Territories
from random import randrange
from enum import Enum

class State(Enum):
    PREGAME = 1
    INITIALPLACEMENT = 2
    PLAY = 3
    END = 4

class Phase(Enum):
    NEWTROOPS = 1
    ATTACKING = 2
    POSTATTACK = 3
    FINISH = 4

class Game:

    CARDBONUS = [4,6,8,10,12,15,20,25,30,35,40,45,50,55,60]

    def __init__(self, playersArray: {Color:Player}):
        self.__numPlayers = len(playersArray)
        self.__players = playersArray
        self._map = Map()
        self._turnOrder = self.assignTurnOrder()
        self._turn = self._turnOrder[0]
        self._turnPhase = None
        self._gamePhase = State.PREGAME
        self._cardBonus = 0

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
    	assert self._gamePhase == State.INITIALPLACEMENT, "It is not the INITIALPLACEMENT game phase"
    	player = self.__players[self.turn]
        player  = self.__players[playerColorEnum]
        territory = self._map.nodes[territoryName]
        player.placeTroops(1, territory)
        player.removeTroops(1)
        if (all([person.troops == 0 for person in self.__players.values()])):
            self._gamePhase = State.PLAY
            self._turnPhase = Phase.NEWTROOPS
        self.nextTurn()

    def giveTroops(self):
    	assert self._gamePhase == State.PLAY, "It is not PLAY game phase"
    	assert self._turnPhase == Phase.NEWTROOPS, "It is not the NEWTROOPS phase"
    	player = self.__players[self._turn]
        bonusTroops = (len(player.territories) // 3)
        
        # Continent Bonus
        for continent in self._map.continents:
            if all([territory in player.territories for territory in continent.getTerritories()]):
                bonusTroops += continent.points

        # Card Bonus - Need to add mechanism for turning in cards
        giveCardBonus = False
        if(giveCardBonus):
            bonusTroops += self.CARDBONUS[self._cardBonus]
            self._cardBonus += 1

        player.troops = bonusTroops
        self._turnPhase = Phase.ATTACKING

    def fight(self, attackDice, defenseDice):
        defenseLost, attackLost = 0, 0
        for _ in range(len(defenseDice)):
            if attackDice.pop(attackDice.index(max(attackDice))) > defenseDice.pop(defenseDice.index(max(defenseDice))):
                defenseLost += 1
            else:
                attackLost += 1
        return attackLost, defenseLost

    def attack(self, sourceName: str, targetName: str, numTroopsAttacking: int, numTroopsDefending: int):
        player = self.__players[self._turn]
        source = self._map.nodes[sourceName]
        target = self._map.nodes[targetName]
        assert self._turnPhase == Phase.ATTACKING, "It is not the ATTACKING phase"
        assert target in source.getNeighbors(), targetName, "is not a neighbor of", sourceName
        assert target.color is not player.color, "You cannot attack yourself"
        assert source.color is player.color, sourcename, "is not your territory"
        assert numTroopsAttacking < source.troops and numTroopsAttacking in (1,2,3), "Number of troops attacking out of range"
        assert numTroopsDefending <= target.troops and numTroopsDefending in (1,2), "Number of troops defending out of range"
        attackDice = [randrange(1, 6) for __ in range(numTroopsAttacking)]
        defenseDice = [randrange(1, 6) for __ in range(numTroopsDefending)]
        sourceLost, targetLost = self.fight(attackDice, defenseDice)
        source.removeTroops(sourceLost)
        target.removeTroops(targetLost)
        if not target.troops:
  	  	    self._turnPhase = POSTATTACK

    def postAttack(self, sourceName: str, targetName: str, numTroopsMoving: int, numDice: int):
    	player = self.__players[self._turn]
    	source = self._map.nodes[sourceName]
        target = self._map.nodes[targetName]
        assert self._turnPhase == Phase.POSTATTACK, "It is not the POSTATTACK phase"
    	assert numTroopsMoving >= numDice and numTroopsMoving < player.troops, "You cannot move this many troops"
    	source.removeTroops(numTroopsMoving)
    	target.addTroops(numTroopsMoving)



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


