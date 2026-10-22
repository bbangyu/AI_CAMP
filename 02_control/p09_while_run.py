print("="*50)
print("while문")
print("="*50)

i = 1

while i <= 5:
    print(i)
    i += 1

print("="*50)
print("1. 사용자 입력 반복하기")
print("="*50)


# total = 0

# while True:
#     number = int(input('숫자를 입력하세요(0:종료):'))

#     if 0 == number:
#         break

#     total += number;

# print(f'합계: {total}')
# print('프로그램 종료')

print("="*50)
print("2. 1 ~ 10 호출 출력 하기")
print("="*50)

i = 0

while i<10:
    i += 1

    # 짝수
    if i % 2 == 0:
        continue

    print(i)