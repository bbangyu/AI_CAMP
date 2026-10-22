print("="*50)
print("반복문")
print("="*50)

print('Python')
print('Python')
print('Python')
print('Python')
print('Python')

print('-'*50)

for i in range(5):
    print('Python')

print("="*50)
print("1. range() 함수")
print("="*50)

#range
for i in range(5):
    print(i)

print('-'*50)

#range(start,stop)
for i in range(1,6):
    print(i)

print('-'*50)

#range(start,stop,step)
for i in range(1,10,2):
    print(i)

print("="*50)
print("2. 문자열 반복하기")
print("="*50)

for ch in "Python":
    print(ch)

print("="*50)
print("3. 리스트 반복하기")
print("="*50)

fruits = ["사과","바나나","복숭아"]

for fruit in fruits:
    print(fruit)

print("="*50)
print("4. 반복하면서 계산하기")
print("="*50)

scores = [80,90,70,85]

total = 0

for score in scores:
    total += score
    print(f'score:{score}')
    print(f'total:{total}')

print('합계:',total)

print("="*50)
print("5. 조건문과 함께 사용하기")
print("="*50)

for i in range(1,11):
    if i % 2 == 0:
        print(i)

print("="*50)
print("6. 구구단 만들기")
print("="*50)

dan = 2

for i in range(1,10):
        print(f'{dan}*{i}={dan*i}')