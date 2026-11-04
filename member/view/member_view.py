# member_view.py
"""
회원 관리 View
### 회원 관리 ###
1. 회원 등록
2. 회원 전체 조회
3. 회원 단건 조회
4. 회원 삭제
5. 회원 수정
6. 종료

Validation
    - 필수 입력 검사
    - 공백 입력 검사
    - Member 객체 생성시 유효성 검사
 """

from common.log_config import setup_logging
from member.model.member import Member
from member.dao.member_dao import MemberDao
from member.service.member_service import MemberSevice
from member.controller.member_controller import MemberController
import logging

setup_logging()

logger = logging.getLogger(__name__)

class MemberView:
    def __init__(self, controller: MemberSevice) -> None:
        self.controller = controller

        # 단건 조회
    def input_select_one(self) -> None:
        """
        회원 단건 조회 화면
        """
        print("[회원 단건 조회]")

        member_id = self.input_required("조회할 회원 ID")

        member = self.controller.do_select_one(member_id)

        if member is not None:
            #print(member)
            logger.debug("member:%s",member)
        else:
            print("회원을 찾을 수 없습니다.")   

    # 메뉴
    def show_menu(self) -> None:
        """회원 관리 메뉴 출력"""
        print("\n================ 회원관리 ==================")
        print("1. 회원 등록      ")
        print("2. 회원 전체 조회 ")
        print("3. 회원 단건 조회 ")
        print("4. 회원 삭제     ")
        print("5. 회원 수정     ")
        print("0. 종료         ")

    @staticmethod
    def input_required(prompt:str) ->str:
        """
        필수 입력값 검사
        
        빈 문자열이나 공백을 입려하면 다시 입력 받습니다.
        """
        while True:
            value = input(f"{prompt}: ").strip()

            if value:
                return value

            print("[입력 오류] 필수 입력 항목 입니다. 다시 입력하세요.")

            print("value: ",value)


    def input_save(self) -> None:
        """ 회원 등록 화면 """
        print("[회원 등록]")

        # 필수 입력 검사
        # 회원ID
        member_id = self.input_required("회원ID")

        # 회원 ID 중복검사
        if self.controller.do_select_one(member_id) is not None:
            print("이미 등록된 회원ID입니다.")
            return
        
        # 회원 이름, 이메일, 비밀번호, 
        name = self.input_required("이름")
        email = self.input_required("이메일")
        password = self.input_required("비밀번호")
        
        # print("member_id: ",member_id)
        # print("email: ",email)
        # print("password: ",password)

        try:
            # Member 객체 생성
            member = Member(
                member_id = member_id,
                name = name,
                email = email,
                password = password
            )

            # Controller에 회원등록 요청
            result = self.controller.do_save(member)

            if result:
                print("회원 등록 성공!")
            else:
                print("회원 등록 실패!")

        except(ValueError, TypeError) as e:
            print(f"[입력 오류] {e}")

    # 단건 조회
    def input_select_one(self) -> None:
        """
        회원 단건 조회 화면
        """
        print("[회원 단건 조회]")

        member_id = self.input_required("조회할 회원 ID")
        member = self.controller.do_select_one(member_id)
        if member is not None:
            print(member)
        else:
            print("회원을 찾을 수 없습니다.")

    def input_delete(self) -> None:
        """ 
            회원 삭제 화면
        """
        print("\n[회원 삭제]")

        member_id = self.input_required("삭제할 회원 ID")

        result = self.controller.do_delete(member_id)

        if result:
            print("회원 삭제 성공")
        else:
            print("회원을 찾을 수 없습니다.")

    def input_update(self) -> None:
        """
        회원정보 수정 화면
        """
        print("[회원정보 수정]")

        member_id = self.input_required("수정할 회원 ID")

        # 회원 단건조회
        member = self.controller.do_select_one(member_id)

        if member is None:
            print("회원을 찾을 수 없습니다.")
            return
        
        print(f"현재 회원 정보: {member}")

        # 수정할 정보 입력
        name = input("새 이름(변경하지 않으려면 Enter): ").strip()
        email = input("새 이메일(변경하지 않으려면 Enter): ").strip()
        password = input("새 비밀번호(변경하지 않으려면 Enter): ").strip()

        # 기존 정보를 유지하면서 수정
        updated_member = Member(
            member_id = member.member_id,
            name = name if name else member.name,
            email = email if email else member.email,
            password = password if password else member.password

        )

        # Controller에 회원 정보 수정 요청
        result = self.controller.do_update(updated_member)

        if result:
            print("회원 정보 수정 성공")
        else:
            print("회원 정보 수정 실패")

    def show_retrieve(self) -> None:
        """ 회원 전체 조회 화면 """
        print("\n회원 전체 조회")

        members = self.controller.do_retrieve()

        if not members:
            print("등록된 회원이 없습니다.")
            return
        for member in members:
            print(member)
        
    # 실행 순서
    def run(self) -> None:
        """ 회원 관리 프로그램 실행 """
        actions = {
            "1": self.input_save, 
            "2": self.show_retrieve,
            "3": self.input_select_one,
            "4": self.input_delete,
            "5": self.input_update
        }
        # 메뉴
        while True:
            self.show_menu()

            try:
                choice = input("메뉴 선택: ").strip()
                # print("choice: ", choice)

                if choice == "0":
                    print("프로그램을 종료합니다.")
                    break

                action = actions.get(choice)
                # print("action: ",action)

                action()

            except (EOFError, KeyboardInterrupt):
                print("\n 프로그램을 종료 합니다.")
                break


def main():
    """프로그램 시작"""
    # DAO 객체 생성
    dao = MemberDao()

    # Service 객체 생성
    service = MemberSevice(dao)

    # Constroller에 Service 주입
    controller = MemberController(service)

    # View에 COntroller 주입
    view = MemberView(controller)

    # 회원관리 프로그램 실행
    view.run()
    


if __name__ == "__main__":
    main()
        