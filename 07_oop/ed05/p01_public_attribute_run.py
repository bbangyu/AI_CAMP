# p01_public_attribute_run.py

class Member:

    def __init__(self, member_id:str, name:str):
        self.member_id = member_id
        self.name = name


def main():
    member = Member("user01","홍길동")

    print("회원ID:",member.member_id)
    print("이름:",member.name)

    member.name = "김철수"

    print("변경 이름:",member.name)

if __name__ == "__main__":
    main()