# member.py
# 회원등록, 조회, 삭제, 전체 조회
# 함수 목록 : ctrl + shift + O
members = []

def do_delete(user_id):
    """회원 아이디로 삭제 합니다."""
    # 회원이 있는지 확인
    member = do_select_one(user_id)

    if member is None:
        return False

    members.remove(member)

    return True

def do_select_one(user_id):
    """
        회원 아이디로 조회합니다.
        Args:

        user_id(str) : 회원 ID

        Return:
            member : {'user_id': 'pcwk01', 'name': '이상무', 'email': 'jamesol@naver.com'}
    """
        #전체 리스트 순회
        # user_id가 있는지 찾는다. 있으면 member를 돌려 준다.

        #없으면 None을 돌려 준다.
    for member in members:
        if member ['user_id'] == user_id:
            return member

    return None

def do_save(user_id, name, email):
    """
        회원을 등록 합니다.

        Args:
            user_id(str) : 회원ID
            name(str) : 이름
            eamil(str) : 이메일

        Return:
            True: 등록 성공
            False : 등록 실패
    """

    # 기존 회원ID 존재 확인
    for member in members:
        if member['user_id'] == user_id:
            return False

    # 회원정보 dict 생성
    member = {
        "user_id": user_id,
        "name": name,
        "email": email
    }
    # 회원 dict를 meber list에 추가
    members.append(member)

    return True

def do_retrieve():
    """전체 회원 목록을 반환 합니다."""

    return members.copy()


if __name__ == '__main__':
    print(f'members:{members}')

    is_saved01 = do_save('pcwk01','이상무','jamesol@naver.com')
    is_saved02 = do_save('pcwk01','이상무','jamesol@naver.com')

    print(f'is_saved:{is_saved01}')
    print(f'is_saved:{is_saved02}')
    print(f'members:{do_retrieve()}')