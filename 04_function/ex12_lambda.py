print("="*50)
print("2. 학생 점수에 따른 합격 여부 판정")
print("="*50)

# 학생 점수를 전달 받아 60점 이상이면 “합격”, 
# 미만이면 “불합격”을 반환하는 Lambda 함수를 작성하세요.

check_pass = lambda score : "합격" if score >= 60 else "불합격"

print(check_pass(85))
print(check_pass(45))
print(check_pass(60))