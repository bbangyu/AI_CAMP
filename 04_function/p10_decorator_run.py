print("="*50)
print("데코레이터")
print("="*50)

def decorator(func):

    def wrapper():
        print("함수 실행 시작")

        func()

        print("함수 실행 종료")

    return wrapper

@decorator
def hello():
    print('Hello Python')

hello()

# hello = decorator(hello)

# hello

print("="*50)
print("1. 함수 일반화 적용하기: 매개변수, return")
print("="*50)

from functools import wraps


def log(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print('함수 실행 시작')

        result = func(*args, **kwargs)

        print('함수 실행 종료')
        return result

    return wrapper

@log    
def add(a,b):
    return a+b


result = add(15,17)
print("결과:", result)