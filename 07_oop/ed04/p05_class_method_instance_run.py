# p05_class_method_instance_run.py
class Member:

    company_name = "PCWK Academy"

    def __init__(self,member_id,name):
        self.member_id = member_id
        self.name = name

    @classmethod
    def show_member(cls,member):
        #print(f'회사명: {self.comapny_name}')
        print(f'회사명: {Member.company_name}')
        print(f'회원ID: {member.member_id}')
        print(f'이름: {member.name}')

def main():

    member = Member("user01", "이상무")

    member.show_member(member)

if __name__ == "__main__":
    main()