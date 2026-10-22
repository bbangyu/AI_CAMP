import member



def do_save():
    print(f'do_save()')

    is_saved = member.do_save('pcwk01','이상무','jamesol@naver.com')

    if is_saved == True:
        print('등록 성공')
    else:
        print('등록 실패')

    print(f'등록 회원 조회: {member.do_retrieve()}')

def do_select_one():
    print(f'do_select_one()')

    member_data=member.do_select_one('pcwk01')

    if member_data is None:
        print('단건 조회 실패')
    else:
        print('단건 조회 성공')


    print(f'member_data:{member_data}')

def do_delete():
    print(f'do_delete()')

    is_deleted = member.do_delete('pcwk01')

    if is_deleted == True:
        print('삭제 성공')
    else:
        print('삭제 실패')

    #전체 데이터 조회
    print(f"삭제 이후 데이터: {member.do_retrieve()}")
    
def main():
    print(f'main()')

    do_save()     #등록
    do_select_one() #단건조회
    do_delete()     #단건삭제

if __name__ == '__main__':
    main()