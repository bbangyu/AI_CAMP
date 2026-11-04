from typing import Protocol

class MemberDaoProtocol(Protocol):

    def do_save(self, member:str)->int:
        ...

class JsonMemberDao:
    def do_save(self, member:str)->int:
        print("JSON 저장:", member)
        return 1

class DatabaseMemberDao:
    def do_save(self, member:str)->int:
            print("DB 저장:", member)
            return 1

class MemberService:
     def __init__(self, member_dao:MemberDaoProtocol):
          self.member_dao = member_dao

     def register(self, member:str) ->int:
          return self.member_dao.do_save(member)

def main():
    service = MemberService(JsonMemberDao())
    service.register("김철수")

    service = MemberService(DatabaseMemberDao())
    service.register("이영희")


if __name__ == "__main__":
    main()