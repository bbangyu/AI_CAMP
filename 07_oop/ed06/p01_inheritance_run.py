# 부모 클래스
class Animal:

    def eat(self):
        print("먹이를 먹습니다.")

# 자식 클래스
class Dog(Animal):

    def bark(self):
        print("멍멍!")


def main():
    dog = Dog()

    dog.eat()
    dog.bark()


if __name__ == "__main__":
    main()