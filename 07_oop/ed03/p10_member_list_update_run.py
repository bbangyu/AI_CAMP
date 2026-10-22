# p10_member_list_update_run.py


class Member:
    # 소스 정리: shift + alt + f
    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email

    def change_name(self, new_name):
        self.name = new_name

    def show_info(self):
        print(f"{self.member_id} / {self.name} / {self.email}")  


def main():
    members = [
        Member("user01", "이상무", "jamesol9@naver.com"),
        Member("user02", "이영희", "jamesol8@naver.com"),
        Member("user03", "김철수", "jamesol7@naver.com"),
    ]

    # 이영희(user02) -> 김영수

    for member in members:

        if member.member_id == "user02":
           member.change_name('김영수')
           break

    print("===수정 후 회원 목록===")
    for member in members:
        member.show_info()


if __name__ == "__main__":
    main()
# p10_member_list_update_run.py


class Member:
    # 소스 정리: shift + alt + f
    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email

    def change_name(self, new_name):
        self.name = new_name

    def show_info(self):
        print(f"{self.member_id} / {self.name} / {self.email}")  


def main():
    members = [
        Member("user01", "이상무", "jamesol9@naver.com"),
        Member("user02", "이영희", "jamesol8@naver.com"),
        Member("user03", "김철수", "jamesol7@naver.com"),
    ]

    # 이영희(user02) -> 김영수

    for member in members:

        if member.member_id == "user02":
           member.change_name('김영수')
           break

    print("===수정 후 회원 목록===")
    for member in members:
        member.show_info()


if __name__ == "__main__":
    main()
