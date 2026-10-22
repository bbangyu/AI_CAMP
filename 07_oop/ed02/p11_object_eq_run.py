# p11_object_eq_run.py

class Student:

    def __init__(self, name, score):
    
        self.name = name
        self.score = score

    # def __eq__(self, other):

    #     if not isinstance(other,Student):
    #         return NotImplemented

    #     return(
    #         self.name == other.name
    #         and
    #         self.score == other.score
    #     )


def main():

    student1 = Student("이상무",90)
    student2 = Student("이상무",90)
    student3 = student1

    print("student1 == student2:",student1 == student2)
    print("student1 is student2:",student1 is student2)

    print("student1 == student3:",student1 == student3)
    print("student1 is student3:",student1 is student3)



if __name__ == "__main__":
    main()