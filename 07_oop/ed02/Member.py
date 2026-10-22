class Member:

    def __init__(self
                 ,member_id
                 ,name
                 ,email
                 ,reg_date
                ,password
                ,role='USER'
                ):
        if not member_id.strip():
            raise ValueError("회원ID는 필수입니다.")

        if not name.strip():
            raise ValueError("이름은 필수입니다.")

        if "@" not in email:
            raise ValueError("이메일 형식이 올바르지 않습니다.") 

        self.member_id = member_id
        self.name      = name
        self.email     = email
        self.reg_date  = reg_date
        self.role      = role
        self.password  = password
        
    def show_info(self):
        print(f"회원ID: {self.member_id}")
        print(f"이름: {self.name     }")
        print(f"이메일: {self.email    }")
        print(f"가입일: {self.reg_date }")
        print(f"권한: {self.role     }")
        print(f"비번: {self.password }")
        print("="*50)

def main():
    member1 = Member("pcwk01","이상무01","jamesol@naver.com","2026/10-20","USER","4321a")

    member2 = Member("pcwk02","이상무02","jamesol@naver.com","2026/10-20","ADMIN","4321a")

    member1.show_info()
    member2.show_info()

if __name__ == "__main__":
    main()