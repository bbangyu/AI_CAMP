# p12_init_run.py

class Member:
    pass


def main():
    member = Member

    member.member_id = "pcwk01"
    member.name = "이상무"
    member.email = "jamsol@naver.com"

    print(member.name)


if __name__ == "__main__":
    main()