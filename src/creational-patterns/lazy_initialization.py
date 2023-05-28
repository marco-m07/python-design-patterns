"""
Goal:
    Delaying the creation of an object, the calculation of a value, or some other expensive process until 
    the first time it is needed.
Use cases:
    - Objects that have properties that are rarely used (might improve startup speed).
    - Full initialization of the object involves the execution of expensive operations.
"""

from enum import Enum


class ItemType(Enum):
    
    WATER = "Water"
    CARROT = "Carrot"
    POTATO = "Potato"

class Item:

    """
    Item sold in a grocery store.
    """
    
    def __init__(self, type: ItemType) -> None:
        self._name = str(type.value)

    @property
    def name(self) -> str:
        return self._name

class Items:

    """
    Grocery store items.
    """
    
    def __init__(self) -> None:
        self._items = dict()

    def get_item(self, type: ItemType):

        """
        Factory method to return existing object or
        create a new one.
        """

        print("Retrieving {}...".format(type.value))
        if type in self._items.keys():
            item = self._items[type]
        else:
            # New objecy is initialised only when requested and
            # not already existing.
            item = Item(type)
            self._items[type] = item
        return item
    
    def get_items(self) -> dict:
        return [self._items[item].name for item in self._items]
    
def main():
    items = Items()
    print("Available items: \n{}".format(items.get_items()))
    items.get_item(type=ItemType.CARROT)
    print("Available items: \n{}".format(items.get_items()))
    items.get_item(type=ItemType.WATER)
    print("Available items: \n{}".format(items.get_items()))

if __name__ == "__main__":
    main()
