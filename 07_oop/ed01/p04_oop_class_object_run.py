# p04_oop_class_object_run.py

class Car:

    # 생성자
    def __init__(self,color,model):
        self.color = color
        self.model = model
        self.speed = 0

    # 가속
    def acclerate(self,value):
        self.speed += value

    # 자동차 정보 출력
    def show_info(self):
        print(f'모델명: {self.model}')
        print(f'색상 : {self.color}')
        print(f'속도 : {self.speed}km/h')

def main():

    # 객체 생성
    car1 = Car("흰색", "그랜저")
    car2 = Car("빨간색", "테슬라")

    #메서드 호출
    car1.acclerate(30)
    car2.acclerate(50)

    print("=== 첫 번째 자동차 ===")
    car1.show_info()

    print("\n=== 두 번째 자동차 ===")
    car2.show_info()

    car1 = Car("흰색","그랜저")

    print(type(car1))
    print(isinstance(car1, Car))

    car1.color
    car1.model
    car1.speed


if __name__ == "__main__":
    main()