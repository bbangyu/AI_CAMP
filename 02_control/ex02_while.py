import random

answer = random.randint(1,10)
print(f'answer:{answer}')
while True:
    number = int(input("1~10 숫자를 입력하세요:"))
    if answer == number:
        print('정답입니다!')
        break

    if number < answer:
        print('더 큰 숫자입니다!')
    else:
        print('더 작은 숫자입니다!')