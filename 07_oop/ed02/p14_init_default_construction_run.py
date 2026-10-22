# p14_init_default_construction_run.py

class Member:

    def __init__(self):
        self.member_id = ""
        self.name = ""
        self.email = ""
        self.role = "USER"

    def show_info(self):
        print(f'회원ID: {self.member_id}')
        print(f'이름: {self.name}')
        print(f'이메일: {self.email}')
        print(f'권한: {self.role}')

def main():
    member = Member()
    member.show_info()



if __name__ == "__main__":
    main()