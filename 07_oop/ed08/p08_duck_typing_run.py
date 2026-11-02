# p08_duck_typing_run.py

class Dog:
    def sound(self):
        print("멍멍")

class Robot:
    def sound(self):
        print("삐빅")

def play_sound(obj):
    obj.sound()

def main():
    play_sound(Dog())
    play_sound(Robot())


if __name__ == "__main__":
    main()