# p06_object2_create_run.py

class Student:


    def __init__(self, name, score):
        print("2. __init__() 호출")

        self.name = name
        self.score = score

    def show_info(self):
        print(f'이름: {self.name}')
        print(f'성적: {self.score}')

def main():

    student1 = Student("이상무",90);
    
	#새로운 객체를 생성하지 않음
    student2 = student1

    student2.score = 100

    print("student1 성적:",student1.score)
    print("student2 성적:",student2.score)

    

if __name__ == "__main__":
    main()