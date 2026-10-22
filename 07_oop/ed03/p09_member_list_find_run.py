# p09_member_list_find_run.py


class Member:
    # 소스 정리: shift + alt + f
    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email

    def show_info(self):
        print(
            
            f'{self.member_id} /'
            f'{self.name} /'
            f'{self.email}'
            )

def find_member(members,member_id):

    for member in members:
        if member.member_id == member_id:
            return member

    return None

def main():
    members = [
        Member("user01","이상무","jamesol9@naver.com"),
        Member("user02","이영희","jamesol8@naver.com"),
        Member("user03","김철수","jamesol7@naver.com")
        ]

    member = find_member(members, "user02")

    if member is not None:
        print("회원 검색 성공")
        member.show_info()
    else:
        print("회원이 존재하지 않습니다.")


if __name__ == "__main__":
    main()
