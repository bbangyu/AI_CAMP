# p05_object_create_run.py

class Student:

    def __new__(cls,*args,**kwargs):
        print("1. __new__() 호출")
        return super().__new__(cls)

    def __init__(self, name, score):
        print("2. __init__() 호출")

        self.name = name
        self.score = score

    def show_info(self):
        print(f'이름: {self.name}')
        print(f'성적: {self.score}')

def main():
    print("객체 생성 시작")

    student = Student("이상무",90);

    print("객체 생성 완료")
    student.show_info()

if __name__ == "__main__":
    main()