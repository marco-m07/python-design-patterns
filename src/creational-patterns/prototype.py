"""
Goal:
    It is used to clone a Prototype Object, which is a superclass defining fundamental properties.
Use cases:
    -  When cloning is a cheaper operation than creating a new object.
    -  When the creation necessitates long, expensive calls.
"""

from abc import ABC, abstractmethod
import time
import copy
import datetime


class FifaPlayerPrototype(ABC):

    def __init__(self) -> None:
        time.sleep(3)  # Faking an expensive object creation.
        self.speed = None
        self.dribbling = None
        self.attack = None
        self.defense = None

    @abstractmethod
    def clone(self):
        pass

class Stricker(FifaPlayerPrototype):
    
    def __init__(self, speed: int, dribbling: int, attack: int, defense: int) -> None:
        time.sleep(3)  # Faking an expensive object creation.
        self.speed = speed
        self.dribbling = dribbling
        self.attack = attack
        self.defense = defense

    def clone(self):
        return copy.deepcopy(self)

def main():
    print("Started creating Stricker at: {}".format(datetime.datetime.now()))
    stricker_template = Stricker(70, 74, 87, 35)
    print("Finished creating Stricker at: {}".format(datetime.datetime.now()))
    print("Started creating set of Strickers at: {}".format(datetime.datetime.now()))
    for i in range (1, 4):
        stricker = stricker_template.clone()
        print("Finished creating Stricker at: {}".format(datetime.datetime.now()))
    print("Finished creating set of Strickers at: {}".format(datetime.datetime.now()))

if __name__ == "__main__":
    main()
