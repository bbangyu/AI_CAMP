# p03_parent_child_overriding_run.py

class Member:


    def show_info(self):
        print("일반 회원 정보")



#자식 클래스
class AdminMember(Member):


    def show_info(self):
        super().show_info()
        print("관리자 회원 정보")




def main():

    member = Member()

    admin = AdminMember()

    member.show_info()
    admin.show_info()


    
if __name__ == "__main__":
    main()