# p04_instance_method_cls_var_run.py
class Member:

    company_name = "PCWK Academy"

    def __init__(self,member_id,name):
        self.member_id = member_id
        self.name = name

    def show_info(self):
        #print(f'회사명: {self.comapny_name}')
        print(f'회사명: {self.company_name}')
        print(f'회사명: {Member.company_name}')
        print(f'회사명: {type(self).company_name}')
        print(f'회원ID: {self.member_id}')
        print(f'이름: {self.name}')

def main():

    member = Member("user01", "이상무")

    member.show_info()

if __name__ == "__main__":
    main()