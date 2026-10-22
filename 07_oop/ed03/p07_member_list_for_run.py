# p07_member_list_for_run.py


class Member:
    # 소스 정리: shift + alt + f
    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email

    def show_info(self):
        print(f"{self.member_id} /{self.name} /{self.email}")


def main():
    member_data = [
        ("user01", "이상무", "jamesol9@naver.com"),
        ("user02", "이영희", "jamesol8@naver.com"),
        ("user03", "김철수", "jamesol7@naver.com"),
    ]

    members = []
    

    for member_id, name, email in member_data:
        #print(member_id, name, email)
        member = Member(member_id,name,email)

        members.append(member)
        print("==== 전체 회원 목록 ====")

    for member in members:
        member.show_info()


if __name__ == "__main__":
    main()
