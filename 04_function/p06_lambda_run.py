print("="*50)
print("람다(Lambda)")
print("="*50)


def add(a,b):
    return a+b

result=add(15,17)

print(f'result:{result}')

add_new = lambda a,b: a+b

print(type(add_new))
print(add_new(15,17))

print("="*50)
print("1. Lambda도 함수 객체다.")
print("="*50)

add_new = lambda a,b:a+b

print(type(add_new))

print("="*50)
print("3. Lambda 함수 호출")
print("="*50)

square = lambda x:x ** 2

print(square(5))

print("="*50)
print("4. 두 개 이상의 매개변수도 사용할 수 있습니다.")
print("="*50)

total = lambda a,b,c : a+b+c
print(total(15,17,20))

print("="*50)
print("5. Lambda에서는 return을 작성하지 않는다.")
print("="*50)

def double(x):
    return x * 2

double_new = lambda x: x*2

print("="*50)
print("6. 조건식을 Lambda에 적용")
print("="*50)

# 짝수와 홀수 판단
# def check_even(number):
#     if number % 2 == 0:
#         return "짝수"

#     else:
#         return "홀수"

#Lambda
check_even = lambda number: "짝수" if number % 2 == 0 else "홀수"

print(check_even(10))
print(check_even(9))

print("="*50)
print("7. 고차함수와 Lambda")
print("="*50)

def add(a,b):
    return a+b

def calculate(func,a,b):
    return func(a,b)

result = calculate(lambda a,b:a+b,
                   15,
                   17)

print(result)