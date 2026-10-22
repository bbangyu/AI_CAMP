# p01_self_run.py

class Member:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f'이름: {self.name}')
        print(f'나이: {self.age}')
        print("="*20)


def main():
    member1 = Member("이상무",21)
    member2 = Member("영희",20)

    member1.show_info()
    member2.show_info()

    #객체를 직접 전달
    Member.show_info(member1)

if __name__ == "__main__":
    main()