

class Teacher:
    def __init__(self, name:str)-> None:
        self.name = name

class Student:
    def __init__(self, name:str, teacher:Teacher):
        self.name = name
        self.teacher = teacher

teacher = Teacher("김교수")
student = Student("이상무", teacher)

print(student.teacher.name)