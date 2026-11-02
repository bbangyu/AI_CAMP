# p02_parent_child_construction_run.py

class Parent:

    def __init__(self):
        print("부모 클래스의 생성자")

class Child(Parent):

    def __init__(self):
        super().__init__()
        print("자식 클래스의 생성자")


def main():
    chd = Child()


if __name__ == "__main__":
    main()
