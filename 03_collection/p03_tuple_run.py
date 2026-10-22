print("="*50)
print("튜플(Tuple)")
print("="*50)

student = ("Kim",21,71)
print(student)

#data = (_
data = tuple()

print("="*50)
print(" 1) 요소가 하나인 튜플")
print("="*50)

a= (10)
b = (10,)

print(f'type(a):{type(a)}')
print(f'type(b:{type(b)}')

print("="*50)
print("3. 인덱스로 접근하기" )
print("="*50)

fruits = ('사과','바나나','딸기')

print(f'fruits[0]:{fruits[0]}')
print(f'fruits[1]:{fruits[1]}')
print(f'fruits[-1]:{fruits[1]}')

print("="*50)
print("4. 슬라이싱" )
print("="*50)

number = (10,20,30,40,50)
#number = [시작:종료:step]
#시작 : 포함
#종료 : 미포함

print(number[1:4] )

print("="*50)
print("5. 튜플은 수정할 수 없다." )
print("="*50)

# numbers = (10,20,30)

# numbers[0] = 100

print("="*50)
print("6. 주요 메서드와 내장 함수" )
print("="*50)

scores = (80,90,70,90,85)

print(scores.count(90)) # 2
print(scores.index(90)) # 1

print(len(scores)) # 5
print(sum(scores)) # 415
print(max(scores)) # 90
print(min(scores)) # 70

print("="*50)
print("7. 튜플 패킹과 언패킹" )
print("="*50)

student = ('Kim',21,71)
name, age, score = student

print(name)
print(age)
print(score)