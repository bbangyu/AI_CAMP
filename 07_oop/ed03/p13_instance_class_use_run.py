# p13_instance_class_use_run.py

class Member:

    #클래스 변수
    memeber_count = 0


    def __init__(self,member_id,name ):
        #인스턴스 변수
        self.member_id= member_id
        self.name = name

        #클래스 변수 증가
        Member.memeber_count += 1
        


    def show_info(self):
        print(f"{self.member_id}/{self.name}")

def main():
    print("초기 객체 수:",Member.memeber_count)

    member1 = Member("user01","이상무")
    member2 = Member("user02","김영희")
    member3 = Member("user03","김철수")

    member1.show_info()
    member2.show_info()
    member3.show_info()

    print("생성된 객체 수:", Member.memeber_count)

if __name__ == "__main__":
    main()