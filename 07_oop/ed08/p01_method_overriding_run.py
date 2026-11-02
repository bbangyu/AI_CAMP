
class Parent:
    def show(self):
        print("부모 클래스 메서드")

class Child(Parent):
    def show(self):
        print("자식 클래스 메서드")

def main():
    obj = Child()
    obj.show()


if __name__ == "__main__":
    main()