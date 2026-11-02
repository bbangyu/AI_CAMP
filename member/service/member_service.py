# member_service.py

from member.model.member import Member
from member.dao.member_dao import MemberDao

class MemberSevice:

    # 생성자
    def __init__(self, member_dao:MemberDao)->None:
        self.member_dao:MemberDao = member_dao
        
    def do_update(self,member:Member)->int:
        """ 회원 정보를 수정 서비스 """
        return self.member_dao.do_update(member)

    def do_save(self,member:Member)->int:
        """회원 정보 저장 서비스"""
        return self.member_dao.do_save(member)

    def do_delete(self, member_id:str)->int:
        """ 회원 삭제 서비스"""
        return self.member_dao.do_delete(member_id)

    def do_select_one(self, member_id:str)-> Member|None:
        """회원 단건조회 서비스"""
        return self.member_dao.do_select_one(member_id)

    def do_retrieve(self)->list[Member]:
        """회원 목록 조회"""
        return self.member_dao.do_retrieve()

def main():
    dao = MemberDao()
    service = MemberSevice(dao)

    print("__name__:",__name__)
    print("__package__:",__package__)

    member01 = Member( 
                member_id= "pcwk99",
                name= "이상무99",
                email= "jamesol99@naver.com",
                reg_date= "2026-10-26 16:00:00",
                role= "ADMIN",
                password= "a123456789")    

    print("=== 회원 등록 ===")
    flag=service.do_save(member01)
    if flag == 1:
        print("회원 등록 성공")
    else:
        print("회원 등록 실패")      
   
if __name__ == "__main__":
    main()    
    
