from dataclasses import dataclass


@dataclass
class Member:
    member_id: str
    name: str
    email: str

def main():
    member = Member(member_id="M001",name="김철수",email="jamesol@naver.com")
    membe2 = Member(member_id="M001",name="김철수",email="jamesol@naver.com")

    print(member)
    print(member.name)

    print(member == membe2)


if __name__ == "__main__":
    main()