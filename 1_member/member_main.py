# member_main.py

import member

def main():
    print(f'main()')

    #회원 등록
    member.do_save(user_id='pcwk01', 
                   name="이상무", 
                   email='jamesol@naver.com')
    member.do_save(user_id='pcwk02', 
                   name="이상무2", 
                   email='jamesol@naver.com')

    print('회원 전체 조회:', member.do_retrieve())


    #회원 삭제
    member.do_delete(user_id='pcwk02')
    print('삭제 후:',member.do_retrieve())


if __name__ == "__main__":
    main()