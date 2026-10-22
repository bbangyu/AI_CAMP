# 학생 클래스 정의 

class Student:

    # 생성자 
    def __init__(self, name, score):
        self.name = name
        self.score = score

        # 메서드
    def show_info(self):
        print(f'이름:{self.name}')
        print(f'점수:{self.score}')

def main():
    # 객체 생성
    student1 = Student("홍길동",90)
    student2 = Student("이순희",85)

    # 메서드 호출
    student1.show_info()
    print("="*50)
    student2.show_info()

if __name__ == "__main__":
    main()