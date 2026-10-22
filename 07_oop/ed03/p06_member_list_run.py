# p06_member_list_run.py


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


def main():
    members = [
        Member("user01","이상무","jamesol9@naver.com"),
        Member("user02","이영희","jamesol8@naver.com"),
        Member("user03","김철수","jamesol7@naver.com")
        ]

    print("==== 전체 회원 목록 ====")

    for member in members:
        member.show_info()

    print("전체 회원 수:",len(members))


if __name__ == "__main__":
    main()
