from enum import Enum
from color import Color

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

    VZ = "Venezuela"
    BR = "Brazil"
    P = "Peru"
    AR = "Argentina"

    IS = "Iceland"
    GBR = "Great Britain"
    SC = "Scandinavia"
    NE = "Northern Europe"
    WE = "Western Europe"
    SE = "Southern Europe"
    R = "Russia"

    EG = "Egypt"
    NA = "North Africa"
    EAF = "East Africa"
    CAF = "Central Africa"
    SA = "South Africa"
    MA = "Madagascar"

    IN = "Indonesia"
    NG = "New Guinea"
    WA = "Western Australia"
    EA = "Eastern Australia"

    ME = "Middle East"
    AF = "Afghanistan"
    U = "Ural"
    SI = "Siberia"
    I = "India"
    CH = "China"
    MG = "Mongolia"
    IR = "Irkutsk"
    YA = "Yakutsk"
    K = "Kamchatka"
    JA = "Japan"
    SEA = "Southeast Asia"


class Territory:
    ''' A territory on the map '''

    def __init__(self, name: str):
        self.name = name
        self._troops = 0
        self._neighbors = []
        self._color = None
    
    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color: Color):
        self._color = color

    @property
    def troops(self):
        return self._troops

    def addTroops(self, numTroops: int):
        self._troops += numTroops

    def removeTroops(self, numTroops: int):
        self._troops -= numTroops

    def setNeighbors(self, neighbors: [Territories]):
        self._neighbors = neighbors

    def getTerritoryState(self):
        territoryState = {}
        territoryState["color"] = self._color
        territoryState["troops"] = self._troops
        territoryState["name"] = self.name
        return territoryState

    def getNeighbors(self):
        return self._neighbors
    
