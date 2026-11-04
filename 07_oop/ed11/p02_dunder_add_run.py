# p02_dunder_add_run.py

class Point:
    def __init__(self, x:int, y:int)-> None:
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Point):
            return NotImplemented

        return Point(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

def main():
    p1 = Point(2,3)
    p2 = Point(4,5)

    print(p1+p2)
    
if __name__ == "__main__":
    main()