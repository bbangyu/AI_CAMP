# p05_mro_run.py

class A:
    def hello(self):
        print("A 클래스")

class B:
    def hello(self):
        print("B 클래스")

class C(A,B):
    pass

def main():
    obj = C()
    obj.hello()

    print(C.__mro__)
if __name__ == "__main__":
    main()