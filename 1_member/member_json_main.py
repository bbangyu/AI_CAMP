from member.member_service import (
    load_members,
    register_member,
    save_members
)

# member_json_main.py
def main():
    members = load_members()
    print(f'members:{members}')

    result = register_member(members, "pcwk02", "이상무2")
    print(f'result:{result}')
    

    if result == True:
        save_members(members)
        print("회원등록 완료")
    else:
        print("이미 등록된 회원입니다.")

    print("===회원 목록===")

    for member in members :
        print(member)

if __name__ == "__main__":
    main()