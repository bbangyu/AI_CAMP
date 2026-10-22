

while True:
    print("\n=== 메뉴 ===")
    print("1. 회원 조회")
    print("2. 회원 등록")
    print("3. 종료")

    menu = int(input('메뉴 선택: '))

    if 1 == menu:
        print('회원 조회를 선택했습니다.')

    elif 2 == menu:
        print('회원 등록을 선택했습니다.')

    elif 3 == menu:
        print('프로그램을 종료합니다.')
        break

    else:
        print('잘못된 메뉴입니다.')
