#member_constroller.py
"""
    회원관리 Controller
역할:
- 회원 등록
- 회원 전체 조회
- 회원 단건 조회
- 회원 삭제
- 회원 수정
- MemberService 호출
"""
from member.service.member_service import MemberSevice
from member.model.member import Member

class MemberController:

    def __init__(self,member_service:MemberSevice)-> None:
        
        self. member_service: MemberSevice = member_service

    @staticmethod
    def validate_member_id(member_id:str) -> str:
        """
        회원 ID 유효성 검사
        - 문자열 타입 검사
        - 필수 입력 검사
        - 앞뒤 공백 제거
        """
        if not isinstance(member_id ,str) or not member_id.strip():
                    raise ValueError("회원ID는 필수 입력 항목 입니다.")

        return member_id.strip()

    def do_retrieve(self) -> list[Member]:
         """
            회원 전체 조회
        """
         return self.member_service.do_retrieve()

    def do_update(self, member:Member) -> bool:
        """
        회원 수정 요청
        
        Member 객체 타입을 검사 후
        Service에 수정을 요청
        """
        if not isinstance(member, Member):
            raise TypeError("Member 객체를 전달해야 합니다.")

        return self.member_service.do_update(member) == 1
        

    def do_delete(self, member_id:str) -> bool:
        """
        회원 삭제 요청
        """
        member_id = self.validate_member_id(member_id)
        return self.member_service.do_delete(member_id) == 1

    def do_select_one(self, member_id:str) -> Member|None:
        """
        회원 단건 조회
        """
        member_id = self.validate_member_id(member_id)
        return self.member_service.do_select_one(member_id) 
    
    
    def do_save(self, member: Member) -> bool:
        """
        회원등록
        Member 객체 타입을 검사 후 
        Service에 등록을 요청
        """
        if not isinstance(member, Member):
            raise TypeError("Member 객체를 전달해야 합니다.")

        return self.member_service.do_save(member) == 1
    