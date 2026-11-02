# p09_duck_typing_run.py

class Dog:
    def sound(self):
        print("멍멍")
class Cat:
    def sound(self):
        print("야옹")

class Robot:
    # def sound(self):
    #     print("삐빅")
    pass

def play_sound(obj):
    obj.sound()

def main():
    play_sound(Dog())
    play_sound(Cat())
    play_sound(Robot())


if __name__ == "__main__":
    main()