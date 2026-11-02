# p09_property_run.py

class Member:

    def __init__(self,name:str) -> None:
        self.__name = name

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self,value:str) -> None:

        if not isinstance(value, str):
            raise TypeError("이름은 문자열이어야 합니다.")
        if not value.strip():
            raise ValueError("이름은 필수 입력 입니다.")

        self.__name = value

    @name.deleter
    def name(self) -> None:
        del self.__name

def main():
    member = Member("홍길동")

    print("변경 전")
    print("회원 이름:",member.name)

    member.__name = "김철수"
    print("변경 후:",member.name)

    try:
        member.name = ""
    except ValueError as e:
        print("오류:", e)

if __name__ == "__main__":
    main()