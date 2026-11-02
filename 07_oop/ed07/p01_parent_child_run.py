# p01_parent_child_run.py

class Member:

    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name

    def show_info(self):
        print(f"회원ID: {self.member_id}")
        print(f"이름: {self.name}")


#자식 클래스
class AdminMember(Member):

    def __init__(self, member_id, name, department):
        super().__init__(member_id, name)
        self.dempartment = department

    def manage_members(self):
        print(f"{self.name} 관리자가 회원을 관리합니다.")



def main():
    admin = AdminMember(
        "admil01",
        "이상무",
        "운영팀"
    )

    admin.show_info()

    print(f"부서: {admin.dempartment}")

    admin.manage_members()

    
if __name__ == "__main__":
    main()