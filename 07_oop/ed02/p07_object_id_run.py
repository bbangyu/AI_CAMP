# p07_object_id_run.py

class Student:


    def __init__(self, name, score):
        

        self.name = name
        self.score = score

    def show_info(self):
        print(f'이름: {self.name}')
        print(f'성적: {self.score}')

def main():

    student1 = Student("이상무",90)
    student2 = Student("순희",85)
    student3 = student1

    print("student1:",id(student1))
    print("student2:",id(student2))
    print("student3:",id(student3))

    print("student1과 student2", student1 is student2)
    print("student1과 student3", student1 is student3)

if __name__ == "__main__":
    main()