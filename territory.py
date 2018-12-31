from enum import Enum

class Territories(str, Enum):
    AL = "Alaska"
    NT = "Northern Territory"
    GL = "Greenland"
    ALB = "Alberta"
    ONT = "Ontario"
    EC = "Eastern Canada"
    WUS = "Western United States"
    EUS = "Eastern United States"
    CA = "Central America"


class Territory:
    ''' A territory on the map '''

    def __init__(self, name: str):
        self.name = name
        self._troops = 0
        self._neighbors = []
        self.color = None
    
    def getColor(self):
        return self.color

    def getTroops(self):
        return self._troops

    def addTroops(self, numTroops: int):
        self._troops += numTroops

    def removeTroops(self, numTroops: int):
        self._troops -= numTroops

    def setNeighbors(self, neighbors: [Territories]):
        self._neighbors = neighbors

    def getTerritoryState(self):
        territoryState = {}
        territoryState["color"] = self.getColor()
        territoryState["troops"] = self.getTroops()
        territoryState["name"] = self.name
        return territoryState



class Continent:
    def __init__(self, name, points, territories = []):
        self.name = name
        self.territories = territories
        self.points = points

    def add_territory(self, territory):
        self.territories.append(territory)
    
