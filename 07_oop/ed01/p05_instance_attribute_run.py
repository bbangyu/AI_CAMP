# p05_instance_attribute_run.py

class Car:

    def __init__(self,color,model):
        self.color = color
        self.model = model
        self.speed = 0

def main():
    car1 = Car("흰색","그랜저")
    car2 = Car("빨간색","테슬라")

    print(car1.color) #흰색
    print(car2.color) #빨간색

    car1.speed = 50

    print(car1.speed) #50
    print(car2.speed) #0


if __name__ == "__main__":
    main()