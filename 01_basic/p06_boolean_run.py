print("="*50)
print("01.논리형")
print("="*50)

is_student = True
is_login = False

print(f'is_student: {is_student}')
print(f'is_login: {is_login}')

# Python에서 논리형의 자료형은 bool입니다.
is_student = True
print(f'is_student:{is_student },type:{type(is_student)}')

print("="*50)
print("02.비교 연산의 결과는 bool")
print("="*50)

age = 25
print(age == 25)
print(age > 20)
print(age < 20)

print("="*50)
print("03.문자열 비교 연산의 결과는 bool")
print("="*50)

language = "Python"

print(language == "Python")
print(language == "Java")

result = language == 'Python'

print(f'result:{result},type:{type(result)}')

print("="*50)
print("04.논리 연산")
print("="*50)

# and 두 조건이 **모두 참**일 때 True입니다.
age = 25
has_license = True

print(age >=20 and has_license)

#or : 두 조건 중 하나 이상 참이면 True입니다.
is_admin = False
is_manager = True

print(is_admin or is_manager)

#not : 참과 거짓을 반대로 변경합니다.
is_login = True

print(is_login)
print(not is_login)

print("="*50)
print("05.bool과 조건문")
print("="*50)

is_login = True

if is_login: 
    print('로그인 상태입니다.')

print('프로그램 수행 종료!')

print("="*50)
print("06. bool()함수")
print("="*50)

print(bool(1)) #Tue
print(bool(0)) #False

print(bool("python")) #True
print(bool("")) #False

print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool(None))
print(bool(""))
