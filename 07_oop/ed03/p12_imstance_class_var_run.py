# p12_imstance_class_var_run.py

class Member:

    #클래스 변수
    company_name = "PCWK Academy"

    def __init__(self,member_id,name ):
        #인스턴스 변수
        self.member_id= member_id
        self.name = name


    def show_info(self):
        print(f'회사명: {Member.company_name}')
        print(f"회원ID: {self.member_id}")
        print(f"이름: {self.name}")

        print("-"*20)

def main():

    member1 = Member("user01","이상무")
    member2 = Member("user02","김영희")



    # 클래스 이름 변경 전
    print(member1.company_name)
    print(member2.company_name)

    print("-"*20)
    # 클래스 변수 변경
    Member.company_name = "PCWK IT Academy"

    # 클래스 이름 변경 후
    print(member1.company_name)
    print(member2.company_name)




if __name__ == "__main__":
    main()