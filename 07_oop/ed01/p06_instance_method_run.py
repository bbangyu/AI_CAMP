# p06_instance_method_run.py

class Car:

    def __init__(self,model):
        self.model = model
        self.speed = 0

    def accelerate(self,value):
        """ 가속 """
        self.speed += value

    def stop(self):
        """ 정지 """
        self.speed = 0

def main():
    car1 = Car("그랜저")

    car1.accelerate(30)

    car1.stop()

if __name__ == "__main__":
    main()
