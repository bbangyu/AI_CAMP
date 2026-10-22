# p03_self_cls_run.py
class Member:

    company_name = "PCWK Academy"

    def __init__(self, name):
        self.name = name

    def instance_method(self):
        print("self:",self)
        print("이름:",self.name)

    @classmethod
    def class_method(cls):
        print("cls:",cls)
        print(f'회사명: {cls.company_name}')

def main():

    member = Member("이상무")

    member.instance_method()

    member.class_method()


if __name__ == "__main__":
    main()