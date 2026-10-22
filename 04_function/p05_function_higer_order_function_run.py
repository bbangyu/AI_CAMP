print("="*50)
print("고차 함수(Higer-Order Function)")
print("="*50)

def add(a,b):
		return a+b
		

result = add(10,20)

print(result)

print("="*50)
print("1. 함수 자체를 전달 받는 함수")
print("="*50)

def add(a,b):
	return a+b

def calculate(func,a,b):
	return func(a,b)


result = calculate(add,10,20)

print(result)

print("="*50)
print("2. 함수를 인자로 전달하기")
print("="*50)

def add(a,b):
	return a+b

def subtract(a,b):
	return a-b

def calculate(func,a,b):
	return func(a,b)

print(calculate(add,10,20))
print(calculate(subtract,10,20))

print("="*50)
print("3. 다양한 함수를 전달하기")
print("="*50)

def add(a,b):
	return a+b

def subtract(a,b):
	return a-b

def multiply(a,b):
	return a*b

def divide(a,b):
    return(a/b)

def calculate(func,a,b):
	return func(a,b)

print(calculate(add,10,20))
print(calculate(subtract,10,20))
print(calculate(multiply,10,20))
print(calculate(divide,10,20))

print("="*50)
print("4. 함수를 반환하는 고차 함수")
print("="*50)

def create_greeting():

    def hello():
        print('Hello Python')

    return hello

func = create_greeting()

func()

print("="*50)
print("5. 함수를 인자로 받고 함수도 반환하기")
print("="*50)

def decorate(func):

    def wapper():
        print("함수 실행 전")
        func()
        print("함수 실행 후")
    #함수 객체 자체를 반환
    return wapper

print("="*50)
print("6.1 Python의 대표적인 고차 함수: map( )")
print("="*50)

numbers = [1,2,3,4,5]

def square(x):
    return x ** 2

result = map(lambda x : x**2,numbers)

print(list(result))

print("="*50)
print("6.1 Python의 대표적인 고차 함수: filter( )")
print("="*50)

numbers = [1,2,3,4,5]

def is_even(x):
	return x % 2 == 0


result = filter(is_even,numbers)

print(list(result))