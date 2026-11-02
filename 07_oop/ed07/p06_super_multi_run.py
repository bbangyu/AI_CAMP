# p06_super_multi_run.py

class A:

    def hello(self):
        print("A.hello()")

class B(A):

    def hello(self):
        print("B.hellO()")
        super().hello()

class C(A):

    def hello(self):
        print("C.hellO()")
        super().hello()

class D(B,C):

    def hello(self):
        print("D.hellO()")
        super().hello()

def main():
    obj = D()
    obj.hello()

    print([ cls.__name__ for cls in D.mro()])

if __name__ == "__main__":
    main()