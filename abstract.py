from abc import ABC, abstractmethod

class Shape(ABC):
    

    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius


    def calculate_perimeter(self):
        return 2 * 3.1466 * self.radius
        

    def calculate_area(self):
        return 3.1466 * (self.radius ** 2)


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height


    def calculate_perimeter(self):
        return 2 * (self.width + self.height)
    

    def calculate_area(self):
        return self.width * self.height
    



class Square(Shape):
    def __init__ (self, side):
        self.side = side


    def calculate_perimeter(self):
        return 4* self.side
    
    def calculate_area(self):
        return self.side ** 2
    


circle = Circle(5)
print ("Circle")
print ("Area",(circle.calculate_area(),))
print("Perimeter", (circle.calculate_perimeter(),2))

rectangle = Rectangle(4,6)
print("Rectangle")
print ("Area", (rectangle.calculate_area()))
print ("Perimeter", (rectangle.calculate_perimeter()))

square = Square(3)
print("Square")
print ("Area", (square.calculate_area()))
print("Perimeter", (square.calculate_perimeter()))