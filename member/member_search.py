# member/member_search.py

#회원 ID로 회원 검색 : find_member

def find_member(members,user_id):
    """회원 ID로 회원 검색"""

    for member in members:
        if member['user_id'] == user_id:
            return member


    return None
