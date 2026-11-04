# p01_dunder_method_run.py

class Member:
    def __init__(self, member_id:str, name:str):
        self.member_id = member_id
        self.name = name

    def __str__(self)->str:
        return f"회원:{self.name}({self.member_id})"
    
    def __repr__(self)->str:
        return f"Member(member_id = {self.member_id!r}, name = {self.name!r})"



def main():
    member = Member("M001", "이상무")

    print("member:",member)
    print(repr(member))


if __name__ == "__main__":
    main()