# p07_name_mangling_run.py

class Parent:

    def __init__(self):
        self.__value = 100

    def get_parent_value(self) -> int:
        return self.__value


class Child(Parent):

    def __init__(self):
        super().__init__()
        self.__value = 200

    def get_child_value(self) -> int:
        return self.__value

def main():
    child = Child()

    print("부모 값:",child.get_parent_value())
    print("자식 값:",child.get_child_value())

    print(child.__dict__)
if __name__ == "__main__":
    main()