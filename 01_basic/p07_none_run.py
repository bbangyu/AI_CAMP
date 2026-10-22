print("="*50)
print("01.None")
print("="*50)

result = None

print(f'reseult:{result}')
print(f'result type:{type(result)}')

# None은 언제 사용하는가
predection = None
print(f"예측 결과 전:{predection }")

predection = "고양이"
print(f"예측 결과 후:{predection }")

# None과 문자열 "None"의 차이
a = None
b = "None"

print(f'a={a},type={type(a)}')
print(f'b={b},type={type(b)}')

# None과 0의 차이
score01 = None
score02 = 0

print(f'score01: {score01}, type:{type(score01)}')
print(f'score02: {score02}, type:{type(score02)}')

# None과 빈 문자열의 차이
name01 = None
name02 = ""

print(type(name01))
print(type(name02))

# None인지 확인
result = None

print(result is None)

# None이 아닌지 확인
result = "완료"

print(result is not None)

# 조건문에서 None 확인하기
result = None

if result is None:
    print('아직 결과가 없습니다.')

result = "고양이"

if result is not None:
    print(f'예측 결과:{result}')

# 함수와 None
def hello():
    print("Hello Python")

result = hello()   

print(f'result:{result}')