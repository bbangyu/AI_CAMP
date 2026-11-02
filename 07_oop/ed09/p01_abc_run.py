from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    pass

def main():
    # circle = Circle()
    # shape = Shape()

if __name__ == "__main__":
    main()