# p11_member_validation_email_password_run.py
import re


class Member:
    company_name = "PCWK Academy"

    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name

    # 인스턴스 메서드
    def show_info(self):
        print(f"{self.member_id} / {self.name}")

    # 정적 메서드
    # - 회원ID는 문자열이어야 합니다.
    # - 회원ID는 5자 이상이어야 합니다.
    # - 회원ID는 영문자와 숫자로만 구성해야 합니다.
    @staticmethod
    def validate_member_id(member_id):

        if not isinstance(member_id, str):
            return False

        if len(member_id) < 5:
            return False

        if not member_id.isascii():
            return False

        if not member_id.isalnum():
            return False

        return True

    # 계정@도메인.최상위도메인 형식은 주로 이메일 주소(E-mail Address)의 기본 구조
    @staticmethod
    def validate_email(email):

        if not isinstance(email, str):
            return False
        # jamesol@naver.com
        pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

        return re.fullmatch(pattern, email) is not None

    @staticmethod
    def validate_password(password):

        if not isinstance(password, str):
            return False

        if len(password) < 8:
            return False

        # 알파벳 있는지
        # any(ch.isalpha() for ch in password)
        has_alpha = any(ch.isalpha() for ch in password)
        has_digit = any(ch.isdigit() for ch in password)

        return has_alpha and has_digit


def main():

    passwords = ["1234", "abcdefgh", "123456789", "abc12345", "password1231"]

    for password in passwords:
        result = Member.validate_password(password)
        print(f"{password}: {result}")


    #any()
    print(any([True, False, False]))  #True
    print(any([False, False, False])) #False
    print(any([False, True, True]))   #True


if __name__ == "__main__":
    main()
