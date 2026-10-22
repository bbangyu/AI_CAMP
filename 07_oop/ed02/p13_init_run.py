# p13_init_run.py

class Member:

    def __init__(self,member_id,name,email):
        self.member_id = member_id
        self.name = name
        self.email = email



def main():
    member = Member("pcwk01","이상무","jamsol@naver.com")

    print(member.name)


if __name__ == "__main__":
    main()