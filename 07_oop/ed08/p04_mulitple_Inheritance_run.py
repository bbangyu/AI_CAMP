# p04_mulitple_Inheritance_run.py

class Father:
    def work(self):
        print("아버지는 일을 합니다.")

class Mother:
    def cook(self):
        print("어머니는 요리를 합니다.")

class Child(Father, Mother):
    pass

def main():
    child = Child()
    child.work()
    child.cook()


if __name__ == "__main__":
    main()