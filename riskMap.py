from territory import Territories, Territory
from enum import Enum

class Map:
    """A Risk map respresented as a graph"""

    def __init__(self):
        self.nodes = {
            Territories.AL : Territory("Alaska"),
            Territories.NT : Territory("Northern Territory"),
            Territories.GL : Territory("Greenland"),
            Territories.ALB : Territory("Alberta"),
            Territories.ONT : Territory("Ontario"),
            Territories.EC : Territory("Eastern Canada"),
            Territories.WUS : Territory("Western United States"),
            Territories.EUS : Territory("Eastern United States"),
            Territories.CA : Territory("Central America")

            Territories.VZ : Territory("Venezuela")
            Territories.BR : Territory("Brazil")
            Territories.P : Territory("Peru")
            Territories.AR : Territory("Argentina")

            Territories.IS = Territory("Iceland")
            Territories.GBR = Territory("Great Britain")
            Territories.SC = Territory("Scandinavia")
            Territories.NE = Territory("Northern Europe")
            Territories.WE = Territory("Western Europe")
            Territories.SE = Territory("Southern Europe")
            Territories.R = Territory("Russia")

            Territories.EG = Territory("Egypt")
            Territories.NA = Territory("North Africa")
            Territories.EAF = Territory("East Africa")
            Territories.CAF = Territory("Central Africa")
            Territories.SA = Territory("South Africa")

            Territories.IN = Territory("Indonesia")
            Territories.NG = Territory("New Guinea")
            Territories.WA = Territory("Western Australia")
            Territories.EA = Territory("Eastern Australia")

            Territories.ME = Territory("Middle East")
            Territories.AF = Territory("Afghanistan")
            Territories.U = Territory("Ural")
            Territories.SI = Territory("Siberia")
            Territories.I = Territory("India")
            Territories.CH = Territory("China")
            Territories.MG = Territory("Mongolia")
            Territories.IR = Territory("Irkutsk")
            Territories.YA = Territory("Yakutsk")
            Territories.K = Territory("Kamchatka")
            Territories.JA = Territory("Japan")
            Territories.SEA = Territory("Southeast Asia")
        }

        self.nodes[Territories.AL].setNeighbors([Territories.NT, Territories.ALB])
        self.nodes[Territories.NT].setNeighbors([Territories.AL, Territories.ALB, Territories.GL, Territories.ONT])
        self.nodes[Territories.ALB].setNeighbors([Territories.AL, Territories.NT, Territories.ONT, Territories.WUS])
        self.nodes[Territories.GL].setNeighbors([Territories.NT, Territories.ONT, Territories.EC])
        self.nodes[Territories.ONT].setNeighbors([Territories.NT, Territories.ALB, Territories.GL, Territories.EC, Territories.EUS, Territories.EC, Territories.WUS])
        self.nodes[Territories.EC].setNeighbors([Territories.GL, Territories.ONT, Territories.EUS])
        self.nodes[Territories.WUS].setNeighbors([Territories.ALB, Territories.ONT, Territories.EUS, Territories.CA])
        self.nodes[Territories.CA].setNeighbors([Territories.WUS, Territories.EUS])

        self.continents = {
            Continents.NA : Continent("North America", 5)
            Continents.SA : Continent("South America", 2)
            Continents.EU : Continent("Europe", 5)
            Continents.AS : Continent("Asia", 7)
            Continents.AF : Continent("Africa", 3)
            Continents.AU : Continent("Australia", 2)
        }

        self.continents[Continents.NA].setTerritories([Territories.AL,Territories.NT,Territories.GL,Territories.ALB,Territories.ONT,Territories.EC,Territories.WUS,Territories.EUS, Territories.CA])
        self.continents[Continents.SA].setTerritories([Territories.VZ, Territories.BR, Territories.P, Territories.AR])
        self.continents[Continents.EU].setTerritories([Territories.IS, Territories.GBR, Territories.SC, Territories.NE, Territories.WE, Territories.SE, Territories.R])
        self.continents[Continents.AS].setTerritories([Territories.ME, Territories.AF, Territories.U, Territories.SI, Territories.I, Territories.CH, Territories.MG, Territories.IR, Territories.YA, Territories.K, Territories.JA, Territories.SEA])
        self.continents[Continents.AF].setTerritories([Territories.EG, Territories.NA, Territories.EAF, Territories.CAF, Territories.SA])
        self.continents[Continents.AU].setTerritories([Territories.IN, Territories.NG, Territories.WA, Territories.EA])
    def getMapState(self):
        mapState = {}
        for key, node in self.nodes.items():
            mapState[key.value]=node.getTerritoryState()
        return mapState


        # # North America
        # alaska = Territory("Alaska")
        # northernTerritory = Territory("Northern Territory")
        # greenland = Territory("Greenland")
        # alberta = Territory("Alberta")
        # ontario = Territory("Ontario")
        # easternCanada = Territory("Eastern Canada")
        # westernUnitedStates = Territory("Western United States")
        # easternUnitedStates = Territory("Eastern United States")
        # centralAmerica = Territory("Central America")

        # # South America
        # venezuela = Territory("Venezuela")
        # brazil = Territory("Brazil")
        # peru = Territory("Peru")
        # argentina = Territory("Argentina")

        # #Africa
        # northAfrica = Territory("North Africa")
        # egypt = Territory("Egypt")
        # eastAfrica = Territory("East Africa")
        # centralAfrica = Territory("Central Africa")
        # southAfrica = Territory("South Africa")
        # madagascar = Territory("Madagascar")

        # # Australia
        # indonesia = Territory("Indonesia")
        # westernAustralia = Territory("Western Australia")
        # easternAustralia = Territory("Eastern Australia")
        # newGuinea = Territory("New Guinea")

        # # Europe
        # iceland = Territory("iceland")
        # scandinavia = Territory("Scandinavia")
        # greatBritain = Territory("Great Britain")
        # westernEurope = Territory("Western Europe")
        # northernEurope = Territory("Northern Europe")
        # southernEurope = Territory("Southern Europe")
        # russia = Territory("Russia")

        # # Asia
        # middleEast = Territory("Middle East")
        # india = Territory("India")
        # southeastAsia = Territory("Southeast Asia")
        # china = Territory("China")
        # afghanistan = Territory("Afghanistan")
        # ural = Territory("Ural")
        # mongolia = Territory("Mongolia")
        # japan = Territory("Japan")
        # irkutsk = Territory("Irkutsk")
        # siberia = Territory("Siberia")
        # yakutsk = Territory("Yakutsk")
        # kamchatka = Territory("Kamchatka")

class Continent:
    def __init__(self, name, points):
        self.name = name
        self._territories = []
        self.points = points

    def setTerritories(self, territories):
        self._territories = territories

    def getTerritories(self):
        return self._territories

class Continents(Enum):
    NA = "North America"