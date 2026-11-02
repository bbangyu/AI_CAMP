# p04_property_run.py

class Member:

    def __init__(self, member_id:str, name:str):
        self.member_id = member_id
        self._name = name

    def get_name(self) -> str:
        return self._name
    
  
def main():
    member = Member("user01","홍길동")

   # 외부에서 직접 접근 가능
    print(member._name)

    print(member.get_name())

    member._name = "김철수"
    print(member.get_name())
    print("프로그램 종료!")

    
if __name__ == "__main__":
    main()  