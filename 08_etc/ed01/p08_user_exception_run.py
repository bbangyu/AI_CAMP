class MembernotFoundError(Exception):
    """ 회원을 찾을 수 없는 경우 발생 예외 """

    pass

def find_member(member_id:str):
    members = {"hong": "홍길동"}

    if member_id not in members:
        raise MembernotFoundError(
            f"회원을 찾을 수 없습니다.:{member_id}"
        )

    return members[member_id]

try:
    print(find_member("kim"))

except MembernotFoundError as e:
    print(e)