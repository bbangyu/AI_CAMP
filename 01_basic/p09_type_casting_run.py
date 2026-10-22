print("="*50)
print("형변환(Type Casting)")
print("="*50)

data = "100"

print(data)
print(type(data))

data = int(data)
print(f'data:{data},:{type(data)}')

# 형변환이 필요한 이유
a = "10"
b = "20"

print(a+b)

result = int(a) + int(b)

print(f'reuslt:{result}')

# int() - 정수형으로 변환
number = "100"
number = int(number)

print(number)
print(type(number))

#실수도 정수로 변환할 수 있습니다.
number=3.14
print(int(number))

#소수점 이하 처리 : 버림으로 처리
print(int(3.8))
print(int(-3.8))

#문자열을 int변환
# number = "Python"
# print(int(number))

# 실수형 문자열
# number = "3.14"
# print(int(number))

number = "3.14"
result = int(float(number))
print(result)

# float() - 실수형으로 변환
number = "3.14"

number = float(number)

print(number)
print(type(number))

# 정수를 실수로 변환
number = 100
print(float(number))

# str() - 문자열로 변환
age = 21

age = str(age)

print(age)
print(type(age))

#문자열과 숫자를 +로 직접 연결하면
# age = 21

# print('나이:'+age)

age = 21
print('나이:'+str(age))
print('나이:',age)
print(f'나이:{age}') #f-string

#bool() - 논리형으로 변환 -> bool()함수는 값을 True 또는 False로 변환합니다.
print(bool(1))
print(bool(0))     #False
print(bool(0.0))   #False
print(bool('Python'))
print(bool(''))    #False
print(bool(None))  #False
print(bool(False)) #False

print(bool(100))      #True
print(bool(-1))       #True
print(bool("Python")) #True
print(bool("False"))  #True

#자동 형변환
a = 10
b = 2.5

result = a + b

print(result)
print(type(result))