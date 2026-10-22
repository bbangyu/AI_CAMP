print("="*50)
print("일급 객체(First-Class Object)")
print("="*50)

def hello():
    print("Hello, Python")


print(type(hello))

print("="*50)
print("1. 함수를 변수에 저장할 수 있다.")
print("="*50)

func = hello

func()
hello()

print("="*50)
print("2. 함수를 다른 함수의 인자로 전달할 수 있다.")
print("="*50)

def add(a,b):
    return(a+b)

def sub(a,b):
    return a-b


def calculate(func,a,b):
    return func(a,b)


print(calculate(add,10,20))
print(calculate(sub,10,20))

print("="*50)
print("3. 함수를 반환값으로 사용할 수 있다.")
print("="*50)

def outer():

    def inner():
        print('inner 함수 실행')

    return inner

func=outer()

func()

print("="*50)
print("4. 함수를 컬렉션에 저장할 수도 있다.")
print("="*50)

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

operations = {
    "add" : add,
    "sub" : sub
}

print(operations["add"](10,20))
print(operations["sub"](10,20))