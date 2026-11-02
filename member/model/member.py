# member.py
import re
from datetime import datetime
from common.base_dto import BaseDTO

class Member(BaseDTO):
    """회원 정보를 관리하는 모델 클래스 캡슐화 적용"""

    def __init__(
        self,
        member_id: str,
        name: str,
        email: str,
        password: str,
        role: str = "USER",
        reg_date: str | None = None,
    ) -> None:

        self.__member_id = member_id
        self.__name = name
        self.__email = email
        self.__password = password
        self.__role = role
        self.__reg_date = (
            datetime.now().strftime("%Y/%m/%d %H:%M:%S")
            if reg_date is None
            else reg_date
        )

    @property
    def member_id(self) -> str:
        """회원ID 읽기 전용"""
        return self.__member_id

    @property
    def name(self) -> str:
        """이름"""
        return self.__name

    @property
    def email(self) -> str:
        """이메일"""
        return self.__email

    @property
    def password(self) -> str:
        """비밀번호: 평문"""
        return self.__password

    @property
    def role(self) -> str:
        """권한"""
        return self.__role

    @property
    def reg_date(self) -> str:
        """등록일"""
        return self.__reg_date

    # setter
    @member_id.setter
    def member_id(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("회원ID는 필수 문자열입니다.")
        self.password = value

    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("이름은 필수 문자열 입니다.")

        self.__name = value

    @email.setter
    def email(self, value: str) -> None:
        if not self.validate_email(value):
            raise ValueError("이메일 형식을 확인 하세요")

        self.__email = value

    @password.setter
    def password(self, value: str) -> None:
        if not self.validate_password(value):
            raise ValueError("비밀번호를 확인 하세요")
        
        self.__password = value

    @role.setter
    def role(self, value: str) -> None:
        """권한 setter"""
        if not isinstance(value, str) or value not in ["USER", "ADMIN"]:
            raise ValueError("권한은 USER 또는 ADMIN이어야 합니다.")

        self.__role = value

    @reg_date.setter
    def reg_date(self, value: str) -> None:
        """등록일 setter"""
        self.__reg_date = (
            datetime.now().strftime("%Y/%m/%d %H:%M:%S") if value is None else value
        )

    @staticmethod
    def validate_password(password):
        print(f"password:{password}")
        
        if not isinstance(password, str):
            print("isinstance()")
            return False

        if len(password) < 8:
            print("len")
            return False

        # 알파벳 있는지
        # any() : 여러 조건중 하나라도 True이면 True
        has_alpha = any(ch.isalpha() for ch in password)
        has_digit = any(ch.isdigit() for ch in password)
        print(has_alpha,has_digit)
        return has_alpha and has_digit

    @staticmethod
    def validate_email(email: str) -> bool:
        """이메일 검증"""
        if not isinstance(email, str):
            return False

        # jamesol@naver.com
        pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

        return re.fullmatch(pattern, email) is not None

    # Member객체를 딕셔너리로 변환
    
    def to_dict(self)->dict:
        """ Member객체를 딕셔너리로 변환 """
        return   {
            "member_id": self.member_id,
            "name": self.name,
            "email": self.email,
            "reg_date": self.reg_date,
            "role": self.role,
            "password": self.password
        }



    # dict 데이터를 Member 객체로 변환
    @classmethod
    def from_dict(cls, data:dict)-> "Member":
        """ dict 데이터를 Member 객체로 변환 """

        # cls()를 호출하여 Member 객체를 생성
        member = cls(
            member_id = data["member_id"],
            name = data["name"],
            email = data["email"],
            password =  data["password"],
            role     =  data["role"],
            reg_date =  data["reg_date"]
        )
        #print("member:",member)
        return member

    # member_id="user01"
    def __repr__(self) -> str:
        """ """
        return (
            f"Member(  member_id={self.__member_id!r}, "
            f"name={self.__name!r}, "
            f"email={self.__email!r}, "
            f"password={self.__password!r}, "
            f"role={self.__role!r}, "
            f"reg_date={self.__reg_date!r} "
            f")"
        )


def main():
    member = Member("user01", "이상무", "jamesol@naver.com", "a12345678", "USER")

    print(member)


if __name__ == "__main__":
    main()
