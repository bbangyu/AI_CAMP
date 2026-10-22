# p01_instance_method_run.py
class Member:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_name(self):
        print(f"이름: {self.name}")

    def show_age(self):
        print(f"나이: {self.age}")
        

    def show_info(self):
        self.show_name()
        self.show_age()
        print("-"*20)


def main():
    member1 = Member("이상무",21)
    member2 = Member("이상무2",21)
    #일반적인 인스턴스 메서드 호출
    member1.show_info()
    member2.show_info()

if __name__ == "__main__":
    main()