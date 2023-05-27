"""
Goal:
    It allows to have a single construction process that leads to different object
    representations. It separates the construction from the representation of the
    object.
Use cases:
    - Construction of complex objects with multiple optional parameters.
"""

from typing import NamedTuple


class NutritionFacts(NamedTuple):

    calories: int = 0
    fat: int = 0
    sodium: int = 0
    carbohydrate: int = 0
    
class Builder:
    
    # Python provides us with optional arguments. 
    # Builder patter is not really needed.
    def __init__(self, 
                 calories: int, 
                 fat: int = 0, 
                 sodium: int = 0, 
                 carbohydrate: int = 0) -> None:
        
        self.calories = calories
        self.fat = fat
        self.sodium = sodium
        self.carbohydrate = carbohydrate

    def build(self) -> NutritionFacts:
        return NutritionFacts(self.calories, self.fat, self.sodium, self.carbohydrate)

def main():
    nutrition_facts = Builder(calories=100, sodium=10, carbohydrate=4).build()
    print(nutrition_facts)

if __name__ == "__main__":
    main()