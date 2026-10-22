# p07_static_method_run.py

class Calculator:

    @staticmethod
    def add(a,b):
        return a+b

    @staticmethod
    def multiply(a,b):
        return a*b

def main():
    result1 = Calculator.add(15,17)
    result2 = Calculator.multiply(10,20)

    print(f'덧셈: {result1}')
    print(f'곱셈: {result2}')

if __name__ == "__main__":
    main()