from enum import Enum

class Territories(Enum):
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

    def __init__(self, name: str, cont = None):
        self.name = name
        self._troops = 0
        self._neighbors = []
        self.__continent = cont
    
    def getColor(self):
        return self.color

    def getTroops(self):
        return self._troops
    
    def placeTroops(self, troops: int, color: str):
        self._color = color
        self._troops = troops

    def addTroops(self, numTroops: int):
        self._troops += numTroops

    def removeTroops(self, numTroops: int):
        self._troops -= numTroops

    def setNeighbors(self, neighbors: [Territories]):
        self._neighbors = neighbors
        
class Continent:
    def __init__(self, name, territories = [], points):
        self.name = name
        self.territories = territories
        self.points = points
    def add_territory(self, territory):
        self.territory.append(territory)
    
