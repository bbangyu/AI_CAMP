print("="*50)
print("중첩 for 문")
print("="*50)

for i in range(1,4):
    for j in range(1,4):
        print(i,j)

print("="*50)
print("구구단 출력하기")
print("="*50)

for dan in range (2,10):
    print(f'--- {dan}단 ---')

    for i in range(1,10):
        print(f'{dan} * {i} = {dan*i}')#2 * 1 = 2

    print()

print("="*50)
print("2. 구구단 출력하기 단 5단은 건너뛰기.")
print("="*50)

for dan in range (2,10):
    print(f'---{dan}단 ---')
    if dan == 5:
        continue

    for i in range(1,10):
        print(f'{dan} * {i} = {dan*i}')#2 * 1 = 2

    print()

print("="*50)
print("3. 별 출력하기.")
print("="*50)

# star = "*"
# for i in range(1,6):
#     print(f'{star*i}')

# print()

for i in range(1,6):
    for j in range(i):
        print('*',end="")

    print()