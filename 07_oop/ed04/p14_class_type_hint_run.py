# p14_class_type_hint_run.py
class Member:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def show_name(self) -> None:
        print(f"이름: {self.name}")

    def get_name(self) -> str:
        return self.name

    def show_age(self):
        print(f"나이: {self.age}")

    def show_info(self):
        self.show_name()
        self.show_age()
        print("-" * 20)


def main():
    member = Member("이상무", 21)

    print("이름:", member.get_name())
    member.show_name()


if __name__ == "__main__":
    main()
