# p02_init_super_run.py

class Member:

    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name

    def show_info(self):
        print(f"회원ID: {self.member_id}")
        print(f"이름 : {self.name}")

class AdminMember(Member):

    def __init__(self, member_id, name, department):
        # 부모 클래스 생성자 호출
        super().__init__(member_id, name)

        # 자식 클래스의 속성
        self.department = department

    def delete_member(self):
        print("회원 삭제 기능 실행")

def main():
    admin = AdminMember("admin01", "관리자", "시스템 운영팀")

    admin.show_info()
    print("부서: ",admin.department)
    admin.delete_member()


if __name__ == "__main__":
    main()