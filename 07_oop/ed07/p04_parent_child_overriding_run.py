# p04_parent_child_overriding_run.py

class Member:
    pass


#자식 클래스
class AdminMember(Member):
    pass




def main():
    admin = AdminMember()

    print(isinstance(admin, AdminMember))
    print(isinstance(admin, Member))
    print(issubclass(AdminMember,Member))


    
if __name__ == "__main__":
    main()