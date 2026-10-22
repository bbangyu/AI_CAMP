# p07_instance_method_run.py

class Car:

    # 클래스 속성
    wheels = 4

    # 생성자
    def __init__(self, model, color):
        self.model = model
        self.color = color
        self.speed = 0

    # 가속 메서드
    def accelerate(self, value):
        if value > 0 :
            self.speed += value

    # 감속 메서드
    def deceleration(self, value):
        if value > 0 :
            self.speed = max(0, self.speed - value)

    # 정지 메서드
    def stop(self):
        self.speed = 0

    # 자동차 정보 메서드
    def show_info(self):
        print(f'모델명: {self.model}')
        print(f'색상: {self.color}')
        print(f'속도: {self.speed}km/h')
        print(f'바퀴: {self.wheels}')

def main():
    # 객체 생성
    car1 = Car("그랜져","회색")
    car2 = Car("테슬라","빨간색")
    
    Car.wheels = 5
    # 메서드 호출
    car1.accelerate(80)
    car1.deceleration(30)

    car2.accelerate(40)
    print("=== 첫 번째 자동차 ===")
    car1.show_info()

    print("\n=== 두 번째 자동차 ===")
    car2.show_info()

if __name__ == "__main__":
    main()