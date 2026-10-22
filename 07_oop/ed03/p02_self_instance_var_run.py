# p02_self_instance_var_run.py

class Student:

    def __init__(self,name, score):
        self.name = name
        self.score = score

    def show_info(self):
        print(f'이름: {self.name}')
        print(f'점수: {self.score}')
        print("="*20)


def main():
    student1 = Student("홍길동",90)
    student2 = Student("김철수",80)

    student1.show_info()
    student2.show_info()


if __name__ == "__main__":
    main()