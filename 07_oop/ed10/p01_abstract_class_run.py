# p01_abstract_class_run.py

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):

    def __init__(self,radius:float)-> None:
        self.radius = radius

    def area (self) -> float:
        return math.pi * self.radius ** 2

class Rectangle(Shape):

    def __init__(self,width,height):
        self.widht = width
        self.height = height

    def area(self) -> float:
        return self.widht * self.height

class Triangle(Shape):

    def __init__(self,height,widht):
        self.widht = widht
        self.height = height

    def area(self) -> float:
        return self.widht * self.height * 0.5
        super().__init__()



    
def main():
    # 추상 클래스는 스스로 인스턴스 생성 불가
    # shape = Shape()

    # circle = Circle(3)

    # print(f"원 넓이: {circle.area():.2f}")

    shapes : list[Shape] = [Circle(3), Rectangle(10,5), Triangle(10,5)]

    for shape in shapes:
        print(f"{type(shape).__name__}:{shape.area():.2f}")
if __name__ == "__main__":
    main()