# p08_instance_cls_static_method_run.py

class Member:
    company_name = "PCWK Academy"

    def __init__(self,member_id,name):
        self.member_id = member_id
        self.name = name

    # 인스턴스 메서드
    def show_info(self):
        print(f'{self.member_id} / {self.name}')

    # 클래스 메서드
    @classmethod
    def show_company(cls):
        print(f'회사명: {cls.company_name}')

    # 정적 메서드
    @staticmethod
    def is_valid_id(member_id):
        return len(member_id) >= 5

def main():

    member = Member("user01", "이상무")

    #인스턴스 메서드 호출
    member.show_info()

    #클래스 메서드 호출
    Member.show_company()

    #정적 메서드 호출
    result = Member.is_valid_id("user02")
    print('회원id 검증:',result)

if __name__ == "__main__":
    main()