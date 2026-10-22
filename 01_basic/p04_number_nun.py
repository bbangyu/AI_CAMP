# 1. 정수형
age    = 21    #정수형(int)
height = 178.5 #실수형(float)

print("="*50)
print("01. 정수형(int)")
print("="*50)

print("age:",age,type(age))
print("height:",height,type(height))

# 2.숫자형의 기본 연산
print("="*50)
print("02. 숫자형의 기본 연산")
print("="*50)

a = 10
b = 3

print("덧셈:",a+b)
print("뺄셈:",a-b)
print("곱셈:",a*b)
print("나눗셈:",a/b)
print("몫:",a//b)
print("나머지:",a%b)
print("거듭제곱:",a**b)

a = 10
b = 2

result = a/b
print('result:',result,type(result))

print("="*50)
result = 10//3

print(result,type(result))

#int와 float를 함께 계산한다면
a = 10
b = 2.5

result = a + b
print(result,type(result))

price = 1_000_000
quantity = 18
total_price = price * quantity

print(price+3, type(price))
print("total_price:",total_price,type(total_price))

# 지수 표기법
learning_rate = 1e-4 # 1 * 10^-4   ->0.001
e = -4.5e-2          # -4.5 * 10^2 ->-0.045
print(learning_rate  , type(learning_rate  ))
print(e ,type(e))