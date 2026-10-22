print("="*50)
print("1. 학생 정보 조회하기")
print("="*50)

student = {
    "name":"Kim",
    "age":25,
    "score":90
}
print(f'이름:{student.get("name")}')
print(f'나이:{student.get("age")}')
print(f'점수:{student.get("score")}')
