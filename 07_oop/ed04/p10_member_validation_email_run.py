# p10_member_validation_email_run.py
import re

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
    def validate_member_id(member_id):

        if not isinstance(member_id,str):
            return False

        if len(member_id) < 5:
            return False

        if not member_id.isascii():
            return False

        if not member_id.isalnum():
            return False

        return True


    #계정@도메인.최상위도메인 형식은 주로 이메일 주소(E-mail Address)의 기본 구조
    @staticmethod
    def validate_email(email):

        if not isinstance(email, str):
            return False
        #jamesol@naver.com
        pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

        return re.fullmatch(pattern,email) is not None
        
def main():

    emails = [
        "ghkdrbdhks99@naver.com",
        "hone@example.com",
        "invalid-email",
        "test@",
        "Uesr@gmail"
    ]

    for email in emails:

        result = Member.validate_email(email)
        print(f'{email}: {result}')

if __name__ == "__main__":
    main()