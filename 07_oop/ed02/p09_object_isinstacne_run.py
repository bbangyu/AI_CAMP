# p09_object_isinstacne_run.py

class Student:



    def show_info(self):
        print(f'이름: {self.name}')
        print(f'성적: {self.score}')


class Teacher:
    pass    

def main():

    student = Student("이상무",90)

    teacher = Teacher()

    print(isinstance(student, Student))
    print(isinstance(teacher, Teacher))
    print(isinstance(student, Teacher))


if __name__ == "__main__":
    main()