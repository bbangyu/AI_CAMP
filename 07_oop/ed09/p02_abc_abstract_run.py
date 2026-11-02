# p02_abc_abstract_run.py

from abc import ABC, abstractmethod
import math 

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    def show_info(self):
        print("Shape")

class Rectangle(Shape):

    def __init__(self, width:float, height:float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

class Circle(Shape):

    def __init__(self, radius:float)-> None:
        self.radius = radius

    def area(self) -> float:
        return self.radius ** 2 * math.pi
        

def main():
    # rect = Rectangle(10,5)
    # circle = Circle(3)

    
    # print(rect.area())
    # print(circle.area())
    shapes:list[Shape] = [Rectangle(10,5), Circle(3)]

    for shape in shapes:
        print(f"{type(shape).__name__}:{shape.area():.2f}")
        shape.show_info()

if __name__ == "__main__":
    main()