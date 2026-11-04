from dataclasses import dataclass


@dataclass
class Member:
    member_id: str
    name: str
    email: str
    role: str = "USER"
    login_count: int = 0


def main():
    member = Member(member_id="M001", name="김철수", email="jamesol@naver.com")

    print(member)


if __name__ == "__main__":
    main()
