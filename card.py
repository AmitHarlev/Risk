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
