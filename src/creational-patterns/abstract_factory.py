"""
Goal:
    Provides a way to create families of related objects without imposing 
    their concrete classes, by encapsulating a group of individual factories 
    that have a common theme without specifying their concrete classes.
Use cases:
    - Creation of multiple objects that are used together.
"""

class Drink:
    
    def pour(self) -> None:

        """To pour drink."""
        
        pass

class Cola(Drink):
    
    def pour(self) -> None:
        print("Your cola is ready.")

class Water(Drink):
    
    def pour(self) -> None:
        print("Your water is ready.")

class Food:
    
    def cook(self) -> None:

        """To cook food."""
        
        pass

class Pasta(Food):

    def cook(self) -> None:
        print("Your pasta is ready.")

class Sandwich(Food):

    def cook(self) -> None:
        print("Your sandwich is ready.")

class OrderFactory:

    def pour_drink(self) -> None:

        """To pour drink requested as part of the order."""
        
        pass

    def cook_food(self) -> None:

        """To cook food requested as part of the order."""

        pass

class StandardOrderFactory(OrderFactory):

    """
    Standard order (Water + Sandwich).
    """

    def pour_drink(self) -> None:
        drink = Water()
        drink.pour()

    def cook_food(self) -> None:
        food = Sandwich()
        food.cook()

class PremiumOrderFactory(OrderFactory):

    """
    Premium order (Cola + Pasta).
    """

    def pour_drink(self) -> None:
        drink = Cola()
        drink.pour()
    
    def cook_food(self) -> None:
        food = Pasta()
        food.cook()

def main():    
    order1 = StandardOrderFactory()
    print("Standard order is being prepared.")
    order1.pour_drink()
    order1.cook_food()
    order2 = PremiumOrderFactory()
    print("Premium order is being prepared.")
    order2.pour_drink()
    order2.cook_food()

if __name__ == "__main__":
    main()
    