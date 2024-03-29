from game import Game
from player import Player
from color import Color
import json


a = Player(Color.RED)
b = Player(Color.BLUE)
c = Player(Color.GREEN)
d = Player(Color.ORANGE)

players = {
    Color.RED: a,
    Color.BLUE: b,
    Color.GREEN: c,
    Color.ORANGE: d
}

game = Game(players)

game.assignTurnOrder()
game.handOutTerritories()
game.initialTroops()
game.initiateTroops()
for i in range(270):
    game.initialPhasePlaceUnit(game._turn, game.players[game._turn].territories[0])

data = game.getGameState()

json_data = json.dumps(data)

print(json_data)

