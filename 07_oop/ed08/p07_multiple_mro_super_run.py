# p07_multiple_mro_super_run.py

class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")
        super().show()

class C(A):
    def show(self):
        print("C")
        super().show()

class D(B,C):
    def show(self):
        print("D")
        super().show()

def main():
    d = D()
    d.show()



if __name__ == "__main__":
    main()

