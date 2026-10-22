# p09_member_validation_run.py

class Member:
    company_name = "PCWK Academy"

    def __init__(self,member_id,name):
        self.member_id = member_id
        self.name = name

    # 인스턴스 메서드
    def show_info(self):
        print(f'{self.member_id} / {self.name}')

    # 정적 메서드
# - 회원ID는 문자열이어야 합니다.
# - 회원ID는 5자 이상이어야 합니다.
# - 회원ID는 영문자와 숫자로만 구성해야 합니다.
    @staticmethod
    def is_valid_member_id(member_id):

        if not isinstance(member_id,str):
            return False

        if len(member_id) < 5:
            return False

        if not member_id.isascii():
            return False

        if not member_id.isalnum():
            return False

        return True



        
def main():

    member_ids = [
        "user01",
        "abc",
        "user_01",
        "member1234"
    ]

    for member_id in member_ids:
        result = Member.is_valid_member_id(member_id)
        print(f'{member_id}: {result}')


if __name__ == "__main__":
    main()