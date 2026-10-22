print("="*50)
print("2. 두 강의를 모두 수강 하는 학생 찾기")
print("="*50)

python_students = {
	"Kin", "Lee", "Park", "Hong"
}
java_students ={
	"Lee", "Park", "Choi", "Jyng"
}

print(f'두 과목 모두  수강: {python_students & java_students}')