# p05_super_run.py

class Member:

    def __init__(self, member_id, name):

        print("Member 생성자 호출")
        self.member_id = member_id
        self.name = name

    def show_info(self):
        print(f"회원ID: {self.member_id}")
        print(f"이름: {self.name}")


#자식 클래스
class AdminMember(Member):

    def __init__(self, member_id, name, department):
        print("AdminMember 생성자 시작")

      
        self.department = department

        print("AdminMember 생성자 종료")

    def manage_members(self):
        print(f"{self.name} 관리자가 회원을 관리합니다.")

        

def main():
    admin = AdminMember(
        "admil01",
        "이상무",
        "운영팀"
    )

    print(admin.department)
    print(admin.name)
    
if __name__ == "__main__":
    main()