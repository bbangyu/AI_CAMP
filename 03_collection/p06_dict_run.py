print("="*50)
print("딕셔너리")
print("="*50)

student = {
    "name": "Kim",
    "age" : 21,
    "score" : 90
}

print(student)
print(type(student))

data = {}
empty_data = dict()

print(data)
print(type(data))
print(type(empty_data))

print("="*50)
print("1. Key를 이용한 값 조회")
print("="*50)

student = {
    "name": "Kim",
    "age" : 21,
    "score" : 90
}

print(student['name'])
print(student['age'])

print("="*50)
print("2. get()으로 값 조회")
print("="*50)

student = {
    "name": "Kim",
    "age" : 21,
}

print(student.get('name'))  
print(student.get('age'))
print(student.get('age99'))
print(student.get('age99',0)) 

print("="*50)
print("5. 데이터 추가와 수정")
print("="*50)

student = {
    "name": "Kim",
    "age" : 21,
}
print(student)

student['score']=25
print(student)

print("-"*50)
student['age']=19
print(student)

print("="*50)
print("6. 데이터 삭제")
print("="*50)

student = {
    "name": "Kim",
    "age" : 21,
    "score" : 90
}
print(student)

del student ['age']

print(student)

print("-"*50)
score = student.pop("score")
print(score)


print("-"*50)
student.clear()

print(student)


print("="*50)
print("7. keys(), values(), items()")
print("="*50)

student = {
    "name": "Kim",
    "age" : 21,
    "score" : 90
}

print(student.keys())

print("-"*50)

print(student.values())
print("-"*50)

print(student.items())

print("="*50)
print("8. for문과 딕셔너리")
print("="*50)

student = {
    "name": "Kim",
    "age" : 21,
    "score" : 90
}

for key in student:
    print(key)
print("-"*50)

for key, value in student.items():
    print(key,":",value)

print("="*50)
print("9. 여러 학생 데이터 관리")
print("="*50)

students = [
	{ "name": "Kim", "score": 90},
	{ "name": "Lee", "score": 85},
	{ "name": "Park", "score": 95}
]

for student in students:
    print(student['name'],student['score'])
    # print(type(student))
