print("="*50)
print("집합")
print("="*50)

numbers = {10,20,30,20,10}

print(numbers)

print("="*50)
print("2. 집합(set) 생성하기")
print("="*50)

numbers = {10,20,30}
fruits = {'사과','배','딸기'}

numbers = set([10,20,30])
print(f'numbers:{numbers}, type: {type(numbers)}')

data = set()
print(type(data))

data = {}
print(type(data))

print("="*50)
print("3. 중복 데이터 제거")
print("="*50)

numbers = [10,20,30,30,30]
print(type(numbers))

#리스트로 다시 반환할 수도 있습니다.
result =list(set(numbers))

print(result)

print("="*50)
print("4. 요소 추가하기")
print("="*50)

fruits = {'사과','배'}
fruits.add('딸기')

print(fruits)


print("="*50)
print("4. 여러 요소 추가하기: update()")
print("="*50)

fruits.update(['복숭아','멜론'])
print(fruits)

print("="*50)
print("5. 요소 삭제하기")
print("="*50)

fruits = {'사과','배'}
# fruits.remove('사과99')
fruits.discard('사과99')

print(fruits)

print("="*50)
print("6. 집합 연산")
print("="*50)

A = {1,2,3,4}
B = {3,4,5,6}

print(f'합집합: {A | B}')
print(f'합집합: {A.union(B)}')

print('-'*50)
print(f'교집합: {A & B}')
print(f'교집합: {A.intersection(B)}')

print('-'*50)
print(f'차집합: {A - B}')
print(f'차집합: {A.difference(B)}')

print('-'*50)
print(f'대칭 차집합: {A ^ B}')

print("="*50)
print("7. Python내장 메서드")
print("="*50)

numbers = {10,20,30,40,50}
print(len(numbers))
print(sum(numbers))
print(max(numbers))
print(min(numbers))