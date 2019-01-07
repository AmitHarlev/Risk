from enum import Enum

class Pictures(Enum):
    SOLDIER = 0
    KNIGHT = 1
    CANNON = 2


class Card:

    def __init__(self, territory, picture):
        self.__territory = territory
        self.__picture = picture
    
    @property
    def territory(self):
        return self.__territory

    @property
    def picture(self):
        return self.__picture

class Deck:
    def __init__(self):
        self.cards = {
            Territories.AL : Card(Territory("Alaska"), Pictures.SOLDIER),
            Territories.NT : Card(Territory("Northern Territory"), Pictures.CANNON),
            Territories.GL : Card(Territory("Greenland"), Pictures.KNIGHT),
            Territories.ALB : Card(Territory("Alberta"), Pictures.KNIGHT),
            Territories.ONT : Card(Territory("Ontario"), Pictures.KNIGHT),
            Territories.EC : Card(Territory("Eastern Canada"), Pictures.KNIGHT),
            Territories.WUS : Card(Territory("Western United States"), Pictures.CANNON),
            Territories.EUS : Card(Territory("Eastern United States"), Pictures.CANNON),
            Territories.CA : Card(Territory("Central America"), Pictures.CANNON),

            Territories.VZ : Card(Territory("Venezuela"), Pictures.SOLDIER),
            Territories.BR : Card(Territory("Brazil"), Pictures.CANNON),
            Territories.P : Card(Territory("Peru"), Pictures.SOLDIER),
            Territories.AR : Card(Territory("Argentina"), Pictures.SOLDIER),

            Territories.IS : Card(Territory("Iceland"), Pictures.SOLDIER),
            Territories.GBR : Card(Territory("Great Britain"), Pictures.CANNON),
            Territories.SC : Card(Territory("Scandinavia"), Pictures.KNIGHT),
            Territories.NE : Card(Territory("Northern Europe"), Pictures.CANNON),
            Territories.WE : Card(Territory("Western Europe"), Pictures.CANNON),
            Territories.SE : Card(Territory("Southern Europe"), Pictures.CANNON),
            Territories.R : Card(Territory("Russia"), Pictures.KNIGHT),

            Territories.EG : Card(Territory("Egypt"), Pictures.SOLDIER),
            Territories.NA : Card(Territory("North Africa"), Pictures.KNIGHT),
            Territories.EAF : Card(Territory("East Africa"), Pictures.SOLDIER),
            Territories.CAF : Card(Territory("Central Africa"), Pictures.SOLDIER),
            Territories.SA : Card(Territory("South Africa"), Pictures.CANNON),
            Territories.MA : Card(Territory("Madagascar"), Pictures.KNIGHT),

            Territories.IN : Card(Territory("Indonesia"), Pictures.CANNON),
            Territories.NG : Card(Territory("New Guinea"), Pictures.SOLDIER),
            Territories.WA : Card(Territory("Western Australia"), Pictures.CANNON),
            Territories.EA : Card(Territory("Eastern Australia"), Pictures.CANNON),

            Territories.ME : Card(Territory("Middle East"), Pictures.SOLDIER),
            Territories.AF : Card(Territory("Afghanistan"), Pictures.KNIGHT),
            Territories.U : Card(Territory("Ural"), Pictures.KNIGHT),
            Territories.SI : Card(Territory("Siberia"), Pictures.KNIGHT),
            Territories.I : Card(Territory("India"), Pictures.KNIGHT),
            Territories.CH : Card(Territory("China"), Pictures.SOLDIER),
            Territories.MG : Card(Territory("Mongolia"), Pictures.SOLDIER),
            Territories.IR : Card(Territory("Irkutsk"), Pictures.KNIGHT),
            Territories.YA : Card(Territory("Yakutsk"), Pictures.KNIGHT),
            Territories.K : Card(Territory("Kamchatka"), Pictures.SOLDIER),
            Territories.JA : Card(Territory("Japan"), Pictures.CANNON),
            Territories.SEA : Card(Territory("Southeast Asia"), Pictures.SOLDIER),

            Wild_1 : Card()
            Wild_2 : Card()
        }
