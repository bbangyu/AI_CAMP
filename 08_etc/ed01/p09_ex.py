class DuplicateMemberError(Exception):
    """회원ID 중복 예외"""
    pass

class MemberNotFoundError(Exception):
    """회원 조회 실패 예외"""
    pass

from dataclasses import dataclass

@dataclass
class Member:
    member_id : str
    name : str
    email : str

class MemberDao:
    def __init__(self):
        self.members:dict[str,Member] = {}

    def do_save(self, member:Member) -> int:
        if member.member_id in self.members:
            raise DuplicateMemberError(
                f"이미 존재하는 회원 입니다.{member.member_id}"
            )
        self.members[member.member_id] = member
        return 1

    def do_selcet_one(self,member_id:str) -> Member:
        if member_id not in self.members:
            raise MemberNotFoundError(
                f"회원이 존재하지 않는 회원입니다.{member_id}"
            )
        return self.members[member_id]
def main():
    dao = MemberDao()

    member = Member(
        member_id="lee",
        name="이상무",
        email="jamesol@naver.com"
    )

    try:
        dao.do_selcet_one(member.member_id)
        
    except DuplicateMemberError as e:
        print("회원등록 실패:", e)

if __name__ == "__main__":
    main()