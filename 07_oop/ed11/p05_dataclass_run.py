# p05_dataclass_run.py

class Member:
    def __init__(self,member_id:str, name:str, email:str)->None:
        self.member_id = member_id
        self.name = name
        self.email = email


    def __repr__(self):
        return (
            f"Member(member={self.member_id!r}, "
            f"name={self.name!r}, "
            f"email={self.email!r})"
        )    

    def __eq__(self, other):
        if not isinstance(other, Member):
            return NotImplemented

        return(
            self.member_id == other.member_id
            and self.name == other.name
            and self.email == other.email
        )

def main():
    member = Member(member_id="M001",name="김철수",email="jamesol@naver.com")

    print(member)


if __name__ == "__main__":
    main()    