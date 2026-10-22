# p10_object_inhabitance_run.py

class Person:
    pass


class Student(Person):
    pass


def main():

    student = Student()

    print(type(student) is Student)
    print(type(student) is Person)

    print(isinstance(student,Student))
    print(isinstance(student,Person))

if __name__ == "__main__":
    main()