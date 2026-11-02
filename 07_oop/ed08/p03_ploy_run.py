class Animal:

    def sound(self):
        print("동물 소리")

class Dog:

    def sound(self):
        print("멍멍")

class Cat:

    def sound(self):
        print("야옹")

def main():
    animals = [Dog(),Cat()]

    for animal in animals:
        animal.sound()


if __name__ == "__main__":
    main()