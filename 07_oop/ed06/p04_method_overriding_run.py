# p04_method_overriding_run.py


class Member:
    pass

class AdminMember(Member):
    pass

def main():
    admin = AdminMember()

    print(isinstance(admin, AdminMember))
    print(isinstance(admin, Member))

    print(issubclass(AdminMember, Member))

if __name__ == "__main__":
    main()