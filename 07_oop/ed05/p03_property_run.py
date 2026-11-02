# p03_property_run.py

class Member:

    def __init__(self, member_id:str, name:str):
        self.__member_id = member_id
        self.__name = name

    @property
    def member_id(self) -> str:
            return self.__member_id
        

    @property
    def name(self) -> str:
         return self.__name

    @name.setter
    def name(self, value:str) -> None:
         if not isinstance(value, str) or not value.strip():
              raise ValueError("회원 이름은 필수입니다.")

         self.__name = value
          

    # name 필수 처리
    def set_name(self, name:str) -> None:
        if not name.strip():
            raise ValueError("회원 이름은 필수입니다.")
        self.__name = name

def main():
    member = Member("user01","홍길동")

    print("회원ID:",member.member_id)
    print("이름:",member.name)

    # member.member_id = "user02"


    try:
        member.name = "김철수"
        print("이름:",member.name)

    except ValueError as e:
         print("오류:",e)

    print("프로그램 종료!")

    
if __name__ == "__main__":
    main()  