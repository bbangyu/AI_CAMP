print("="*50)
print("Lambda: with map()")
print("="*50)

# 숫자를 제곱하는 일반 함수를 먼저 작성해보겠습니다.

# def square(x):
#     return x ** 2

# numbers = [1,2,3,4,5]

# result = map(square,numbers)

# print(list(result))

numbers = [1,2,3,4,5]

result = map(lambda x : x ** 2,numbers)

print(list(result))

print("="*50)
print("1. Lambda: with filter()")
print("="*50)

#짝수만 선택 하기

numbers = [1,2,3,4,5]

result = filter(lambda x : x % 2 == 0, numbers)

print(list(result))

print("="*50)
print("2. Lambda: with sorted()")
print("="*50)

students = [
    ("Kim",80),
    ("Lee",95),
    ("Park",70)
]

result = sorted(
    students,
    key=lambda student: student[1],
    reverse=True
)

print(result)