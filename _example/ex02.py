## 문제 2. 숫자의 상태 판별하기

# 정수 하나를 입력 받아 양수, 음수, 0 중 어떤 값인지 출력하세요.

number = int(input('정수를 입력하세요: '))

print(f'number:{number},type:{type(number)}')

if number >= 1:
    print("양수입니다.")
elif number == 0:
    print("0입니다.")
else:
    print("음수입니다.")