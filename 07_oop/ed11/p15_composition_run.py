
class Engine:

    def start(self):
        print("엔진 시작")


class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()

car = Car()
car.start()