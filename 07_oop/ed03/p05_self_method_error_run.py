# p05_self_method_error_run.py

class Member:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show_info():
        print("회원 정보 출력")

   

def main():
    member = Member("이상무",21)

    
    member.show_info()


if __name__ == "__main__":
    main()