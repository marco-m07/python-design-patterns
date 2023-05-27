"""
Goal:
    Define a (factory) method to create objects without specifying of which class. Instead of 
    calling directly its constructor, we let the factory decide which object to initialise.
Use cases:
    - Simple object initialisation (few parameters).
    - If we expect the implementation of the interface to frequently change.
"""

class Shape:

    """
    Shape interface.
    """

    def get_area(self) -> int: 

        """Returns the area of the shape."""
        
        pass

class Circle(Shape):

    """
    Implementation of Shape interface that represents a Circle.
    """

    def __init__(self, radius: int) -> None:
        self.radius = radius

    def get_area(self) -> int:
        return self.radius*self.radius
    
class Rectangle(Shape):

    """
    Implementation of Shape interface that represents a Rectangle.
    """

    def __init__(self, height: int, width: int) -> None:
        self.height = height
        self.width = width

    def get_area(self) -> int:
        return self.height*self.width

class ShapeFactory:

    """
    Factory class that offers method to create Shape instances.
    """
    
    def create_shape(self, name: str, **kwargs) -> Shape:
        if name == "circle":
            return Circle(**kwargs)
        elif name == "rectangle":
            return Rectangle(**kwargs)
        else:
            raise ValueError("The shape you are trying to create does not exist.")
        
def main():
    factory = ShapeFactory()
    circle = factory.create_shape(name="circle", radius=2)
    rectangle = factory.create_shape(name="rectangle", height=3, width=4)
    circle_area = circle.get_area()
    rectangle_area = rectangle.get_area()
    print("Are of circle is: {}".format(str(circle_area)))
    print("Are of rectangle is: {}".format(str(rectangle_area)))

if __name__ == "__main__":
    main()

