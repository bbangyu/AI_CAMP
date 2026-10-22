print("="*50)
print("1. 좌표 데이터 저장")
print("="*50)

#지도 좌표(위도, 경도)
location = (37.5665, 126.9780)

x, y = location

print(f'위도:{x}')
print(f'경도:{y}')

print("="*50)
print("2. 함수에서 여러 값 반환")
print("="*50)

def calculate(a,b):
    return a+b, a-b, a*b

result = calculate(10,5)

print(f'result: {result}')
print(f'result[0]: {result[0]}')
print(f'result[-1]: {result[-1]}')

print("="*50)
print("3. 언패킹")
print("="*50)

def calculate(a,b):
    return a+b, a-b, a*b

sum_val, sub_val, mul_val = calculate(10,5)

print(sum_val, sub_val, mul_val)

print("="*50)
print("4. 데이터베이스 조회 결과 표현")
print("="*50)

user = (1, "Kim",21)

user_id, name, age = user

print(user_id)
print(name)
print(age)

print("="*50)
print("5. 데이터베이스 조회 결과 여러행")
print("="*50)

users = [
    (1001,'Kim','Admin'),
    (1002,'Lee','User'),
    (1003,'Park','User')
]

for user_id,name,grade in users:
    print(user_id,name,grade)


print("="*50)
print("6. 프로그램 설정값 관리")
print("="*50)

SERVER = ("localhost",8080)

host, port = SERVER

print(f'서버: {host}')
print(f'포트: {port}')

print("="*50)
print("7. 딕셔너리의 Key로 사용")
print("="*50)

locations = {
    (37.5,126.9):"서울",
    (35.1,129.0):"부산"
}

print(f'locations[(35.1,129.0): {locations[35.1,129.0]}]')

print("="*50)
print("8. enumerate()로 번호와 데이터 함께 처리")
print("="*50)

fruits = ['사과','바나나','딸기']


for index,item in enumerate(fruits,start=1):
    print(index,item)

    
