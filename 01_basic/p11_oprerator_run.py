print("="*50)
print("연산자")
print("="*50)

a = 10
b = 3

result = a+b
print(f'result:{result}')

print("="*50)
print("1. 산술연산자")
print("="*50)

a = 10
b = 3

print('덧셈:',a+b)
print('뺄셈:',a-b)
print('곱셈:',a*b)
print('나눗셈:',a/b)
print('몫:',a//b)
print('나머지:',a%b)
print('거듭제곱:',a**b)

# 짝수와 홀수 판단할 때 많이 사용합니다.
# number = int(input('숫자를 입력하세요:'))

# print(number % 2 == 0)

print("="*50)
print("2. 비교연산자")
print("="*50)

age = 25

print(age == 25)
print(age != 21)
print(age >= 21)

print("="*50)
print("3. 대입연산자")
print("="*50)

price = 10_000
quantity = 3

total_price = price * quantity
print(f'{price}*{quantity}={total_price}')

print("="*50)
print("4. 복합 대입 연산자")
print("="*50)

x = 5
x +=3
print(f'x+=3 -> {x}') # x = x + 3

x = 5
x *=3
print(f'x*=3 -> {x}') # x = x * 3

x = 5
x /=3
print(f'x/=3 -> {x}') # x = x / 3

print("="*50)
print("5. 논리 연산자")
print("="*50)

#and
age = 22
is_member = True

print(age >= 20 and is_member)

#or
is_admin = False
is_manager = True

print(is_admin or is_manager)

#not
is_login = True

print(is_login)
print(not is_login)

print("="*50)
print("6. 멤버십 연산자")
print("="*50)

message = 'Hello Python'

print("Python" in message)
print("Java" in message)

print("Java" not in message)

languages = ['Python','Database','WEB(Htm1,css,JavaScript)']

print("Python" in languages)

print("="*50)
print("7. 식별 연산자")
print("="*50)

result = None

print(result is None)
print(result is not None)

