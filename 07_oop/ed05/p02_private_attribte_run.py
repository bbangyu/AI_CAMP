# p02_private_attribte_run.py

class Member:

    def __init__(self, member_id:str, name:str):
        self.__member_id = member_id
        self.__name = name

    def get_member_id(self) -> str:
        return self.__member_id

    def get_name(self) -> str:
        return self.__name

    # name 필수 처리
    def set_name(self, name:str) -> None:
        if not name.strip():
            raise ValueError("회원 이름은 필수입니다.")
        self.__name = name

def main():
    member = Member("user01","홍길동")

    # AttributeError : 'Member' object has no attribute '__member_id'
    # print("회원ID:",member.__member_id)
    print("회원ID:",member.get_member_id())
    print("회원이름:",member.get_name())
    print("회원ID:",member._Member__name)

    member.set_name("김철수")

    print("변경된 이름:",member.get_name())
    
if __name__ == "__main__":
    main()  