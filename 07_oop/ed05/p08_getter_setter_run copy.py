# p08_getter_setter_run.py

class Member:

    def __init__(self,name:str) -> None:
        self.__name = name

    #Getter
    def get_name(self) -> str:
        return self.__name

    #Setter
    def set_name(self, name:str) -> None:
        self.__name = name

def main():
    member = Member("홍길동")

    print("변경 전:",member.get_name())

    member.set_name("김철수")

    print("변경 후:",member.get_name())

if __name__ == "__main__":
    main()