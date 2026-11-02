# p06_multiple_mro_run.py

class A:
    def shwow(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B,C):
    pass

def main():
    d = D()
    d.show()

    print([cls.__name__ for  cls in D.mro()])

if __name__ == "__main__":
    main()

