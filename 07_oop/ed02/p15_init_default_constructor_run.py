# p15_init_default_constructor_run.py

class Member:
    # 세로 편집 : Ctrl + Art + 위/아래 방향키
    # 화면 분할 : Ctrl + K 누른 뒤 Ctrl + \
    def __init__(self
                ,member_id = ""
                ,name = ""
                ,email = ""
                ,role = "USER"
                ):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.role = role

    def show_info(self):
        print(f'회원ID: {self.member_id}')
        print(f'이름: {self.name}')
        print(f'이메일: {self.email}')
        print(f'권한: {self.role}')
        print("="*50)

def main():
    # 모든 매개변수 생략
    member1 = Member()

    # 일부 매개변수 전달
    member2 = Member("pcwk02","이상무02")

    # 키워드 인수 사용
    member3 = Member(member_id="admin01"
                     ,name="관리자1"
                     ,email="jamsol@naver.com",
                     role="ADMIN")
    
    member1.show_info()
    member2.show_info()
    member3.show_info()


if __name__ == "__main__":
    main()