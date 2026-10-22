# p04_self_method_id_run.py

class Member:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show_id(self):
        print("self id :",id(self))

   

def main():
    member = Member("이상무",21)

    print("member id:",id(member))

    member.show_id()


if __name__ == "__main__":
    main()