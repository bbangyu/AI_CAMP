age = 20
has_ticket = False

if age >= 18:
    if has_ticket:
        print('성년이고 입장 합니다.')
    else:
        print('성년이고 티켓이 없습니다.')
else:
    print('미성년자는 입장할 수 없습니다.')