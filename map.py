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
        }

        self.nodes[Territories.AL].setNeighbors([Territories.NT, Territories.ALB])
        self.nodes[Territories.NT].setNeighbors([Territories.AL, Territories.ALB, Territories.GL, Territories.ONT])
        self.nodes[Territories.ALB].setNeighbors([Territories.AL, Territories.NT, Territories.ONT, Territories.WUS])
        self.nodes[Territories.GL].setNeighbors([Territories.NT, Territories.ONT, Territories.EC])
        self.nodes[Territories.ONT].setNeighbors([Territories.NT, Territories.ALB, Territories.GL, Territories.EC, Territories.EUS, Territories.EC, Territories.WUS])
        self.nodes[Territories.EC].setNeighbors([Territories.GL, Territories.ONT, Territories.EUS])
        self.nodes[Territories.WUS].setNeighbors([Territories.ALB, Territories.ONT, Territories.EUS, Territories.CA])
        self.nodes[Territories.CA].setNeighbors([Territories.WUS, Territories.EUS])

    def getMapState(self):
        mapState = {}
        for key, node in self.nodes.items():
            mapState[key.value]: node.getTerritoryState()
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



