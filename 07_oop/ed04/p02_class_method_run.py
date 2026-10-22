# p02_class_method_run.py
class Member:

    company_name = "PCWK Academy"

    @classmethod
    def show_company(cls):
        print(f'회사명: {cls.company_name}')

def main():

    Member.show_company()


if __name__ == "__main__":
    main()