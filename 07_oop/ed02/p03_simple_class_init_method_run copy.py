# p02_simple_class_init_run.py

# 클래스 선언
class Student:

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def show_info(self):
        print(f'이름: {self.name}')
        print(f'점수: {self.score}')

def main():
    # 객체 생성
    student1 = Student("이상무", 90)
    student2 = Student(name="순희", score=95)

    print("=== 학생1 ===")
    student1.show_info()

    print("\n=== 학생2 ===")
    student2.show_info()

    print(type(student1))
    print(type(student2))

if __name__ == "__main__":
    main()