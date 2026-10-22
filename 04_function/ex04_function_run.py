print("="*50)
print("4. 가변 인자를 이용한 점수 처리")
print("="*50)

# 학생 이름과 여러 개의 점수를 전달 받아 평균과 합격 여부를 반환하는 함수를 작성하세요.

# 점수의 개수는 학생마다 다를 수 있으므로 *args를 사용합니다.



def student_result(name, *scores):
    
    average = sum(scores)/len(scores)
    result = ""

    if average >= 60:
        result = '합격'
    else:
        result = '불합격'
    
    return name, average, result


name, average, result = student_result(
    "Kim", 80, 90, 100
)
print("이름:",name)
print("평균:",average)
print("결과:",result)