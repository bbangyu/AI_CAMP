# member_dao.py

import json
import os
import tempfile
from pathlib import Path
from member.model.member import Member
from common.base_dto import BaseDTO
from common.dao_interface import DaoInterface


class MemberDao(DaoInterface):
    # 생성자
    def __init__(self, file_path: str | Path | None = None) -> None:

        # 기본 저장 경로 : /member/data/members.json
        # __file__ : 현재 실행 중인 Python 모듈 파일의 경로
        if file_path is None:
            file_path = Path(__file__).resolve().parent.parent / "data" / "members.json"

        # file_path: C:\AI_CAMP_20260921\01_PYTHON\WORKSPACE\member\data\members.json
        print("file_path:", file_path)

        # 파일 경로
        self.file_path = file_path

        # 회원 목록
        self.members: list[Member] = []

        # JSON 파일에서 회원정보 읽기
        self.load_json()

    def do_update(self, dto: BaseDTO) -> int:
        """회원 정보를 수정 합니다."""
        if not isinstance(dto, Member):
            raise TypeError("Member 객체만 저장할 수 있습니다.")

        for index, current_member in enumerate(self.members):
            if current_member.member_id == dto.member_id:
                self.members[index] = dto

                try:
                    self.save_json()
                except Exception:
                    self.members[index] = current_member
                    raise
                return 1

        return 0

    def do_retrieve(self) -> list[Member]:
        """전체 회원 목록을 반환 합니다."""
        # Return a shallow copy of the list.
        return self.members.copy()

    def do_delete(self, dto_id: str) -> int:
        """회원 아이디로 삭제"""
        # 회원 아이디 회원 조회
        # 리스트에 있는 회원 삭제
        # 파일에 기록

        print("1. dto_id: ", dto_id)
        member = self.do_select_one(dto_id)
        print("2. member: ", member)
        if member is None:
            return 0

        index = self.members.index(member)
        print("3. index: ", index)
        self.members.pop(index)

        try:
            self.save_json()
        except Exception:
            # 실패시 다시 리스트의 해당 인덱스에 추가
            self.members.insert(index, member)
            raise

        return 1

    def do_select_one(self, dto_id: str) -> Member:
        """회원 아이디로 단건조회"""

        for member in self.members:
            if member.member_id == dto_id:
                return member

        return None

    def do_save(self, dto: BaseDTO) -> int:
        """저장"""

        if not isinstance(dto, Member):
            raise TypeError("Member 객체만 저장할 수 있습니다.")

        # TODO : member_id 중복 체크: do_select_one
        if self.do_select_one(dto_id=dto.member_id) is not None:
            return 0

        self.members.append(dto)

        try:
            self.save_json()
        except Exception:
            self.members.remove(dto)
            raise

        return 1

    def load_json(self) -> None:
        """JSON 파일에서 회원정보 읽어옵니다."""
        # print("load_json()")

        if not self.file_path.exists():
            self.members = []
            return

        with self.file_path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            raise ValueError("회원 JSON 데이터는 리스트여야 합니다.")

        # JSON 딕셔너리를 Member 객체로 변환
        self.members = [Member.from_dict(item) for item in data]

    def save_json(self) -> None:
        """파일 저장(json)"""

        self.file_path.parent.mkdir(parents=True, exist_ok=True)

        # Member객체를 딕셔너리로 변환
        data = [member.to_dict() for member in self.members]

        # JSON 파일에 직접 저장
        with self.file_path.open(mode="w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)


def main():

    dao = MemberDao()
    # print(dao.members)

    member01 = Member(
        member_id="pcwk99",
        name="이상무99",
        email="jamesol99@naver.com",
        reg_date="2026-10-26 16:00:00",
        role="ADMIN",
        password="a123456789",
    )
    # print("=== 회원 수정 ===")
    # # 회원 정보 조회 : pcwk02
    # member = dao.do_select_one("pcwk02")

    # if member:
    #     member.name = "이순희-U9"
    #     member.email = "sunhee_U9@naver.com"
    #     member.password = "a123456789u9"
    #     member.role = "ADMIN"

    #     flag = dao.do_update(member)

    #     if flag == 1:
    #         print("수정 성공")
    #     else:
    #         print("수정 실패1")
    # else:
    #     print("수정 실패2")

    print("=== 회원 전체 조회 ===")
    members = dao.do_retrieve()

    for member in members:
        print(f"- {member}")

    # print("=== 회원 삭제 ===")
    # flag = dao.do_delete(member01.member_id)

    # if flag == 1:
    #     print("삭제 성공")
    # else:
    #     print("삭제 실패")

    print("=== 회원 저장 ===")

    flag = dao.do_save(member01)

    if flag == 1:
        print("회원 등록 성공")
    else:
        print("회원 등록 실패")

    # print("=== 회원 단건 조회 ===")
    # member=dao.do_select_one("pcwk02")

    # if member:
    #     print(f"회원 조회 성공:\n {member}")
    # else:
    #     print("회원 조호 실패")


if __name__ == "__main__":
    main()
