# p02_simple_class_init_run.py

# 클래스 선언
class Student:

    def __init__(self,name,score):
        self.name = name
        self.score = score

def main():
    # 객체 생성

    student1 = Student("이상무",90)
    student2 = Student(name="순희",score=95)

    print("학생1 이름:",student1.name)
    print("학생1 성적:",student1.score)

    print("\n학생2 이름:",student2.name)
    print("학생2 성적:",student2.score)

    print(type(student1))
    print(type(student2))

if __name__ == "__main__":
    main()