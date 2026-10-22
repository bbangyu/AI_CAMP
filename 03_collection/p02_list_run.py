print("="*50)
print(" 1. 리스트 생성")
print("="*50)

#1. 리스트 생성
numbers = [10,20,30,40]
fruits  = ['apple','banana','orange']

data = []
data = list()

print(f'numbers:{numbers}')
print(type(numbers))

print("="*50)
print("2. 리스트는 다양한 자료형을 저장")
print("="*50)

data = [10,3.14,"Python",True, None]
print(f'data: {data}')

print("="*50)
print("3. 인덱스로 요소 접근")
print("="*50)

scores = [80,70,90,85]
print(f'scores[0]: {scores[0]}')
print(f'scores[2]: {scores[2]}')

#음수 인덱스
print(f'scores[-1]: {scores[-1]}')
print(f'scores[-2]: {scores[-2]}')

print("="*50)
print("4. 리스트 슬라이싱")
print("="*50)

number = [10,20,30,40,50]
print(numbers[1:4])

print("="*50)
print("5. 리스트 데이터 수정")
print("="*50)

fruits = ['apple','banana','orange']

print(f'변경전:{fruits}')

fruits[1]='melon'
print(f'변경후: {fruits}')

print("="*50)
print("6. 리스트 데이터 추가")
print("="*50)

fruits = ['apple','banana']

fruits.append('orange')
print(f'fruits:{fruits}')

print("="*50)
print("6. 리스트 데이터 추가: insert()")
print("="*50)

fruits = ['apple','orange']
fruits.insert(1,'banana')
print(f'fruits:{fruits}')

print("="*50)
print("6. 리스트 데이터 추가: extend()")
print("="*50)

a = [10,20]
b = [30,40]

a.extend(b)

print(a)

print("="*50)
print("7. 데이터 삭제 : remove()")
print("="*50)

fruits = ['apple', 'banana', 'orange','banana']
fruits.remove('banana')

print(f'fruits:{fruits}')

print("="*50)
print("7. 데이터 삭제 : pop()")
print("="*50)

fruits = ['apple', 'banana', 'orange','banana']

item = fruits.pop()    

print(f'item: {item}')
print(f'fruits: {fruits}')

print("="*50)
print("7. 데이터 삭제 : del()")
print("="*50)

fruits = ['apple', 'banana', 'orange','banana']

del fruits[0]
print(f'fruits: {fruits}')

print("="*50)
print("8. 리스트 길이")
print("="*50)

scores = [80,90,70,85]
print(len(scores))

print("="*50)
print("9. 리스트 for문")
print("="*50)

scores = [80,90,70,85]

for score in scores:
    print(score)

print("="*50)
print("10. 리스트를 이용한 합계와 평균")
print("="*50)

scores = [80,90,70,85]
total = None

#for score in scores:
#    print(score)
#    total += score

average = total / len(scores)
print(f'합계: {total}')
print(f'평균: {average}:.1f') #소수점 이하 첫째 자리
