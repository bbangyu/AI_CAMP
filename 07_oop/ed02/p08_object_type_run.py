# p08_object_type_run.py

class Student:


    def __init__(self, name, score):
        

        self.name = name
        self.score = score

    def show_info(self):
        print(f'이름: {self.name}')
        print(f'성적: {self.score}')

def main():

    student1 = Student("이상무",90)

    age = 20
    score = 95.5
    name = "영희"
    subjects = ["Python","Oracle"]

    print("student1:",type(student1))
    print(type(age))
    print(type(score))
    print(type(name))
    print(type(subjects))

    print(type(student1) is Student)


if __name__ == "__main__":
    main()