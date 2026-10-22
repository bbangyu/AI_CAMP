print("="*50)
print("1. 학생 성적 분석 함수")
print("="*50)

scores = {80, 95, 70, 85, 90}

#함수 정의:
def analyze_scores(scores):
    '''
    학생들의 점수를 분석 합니다.
    
    Args:
        scores (list): 학생의 점수 리스트
    
    Returns:
        tuple: 합계, 평균, 최고 점수, 최저 점수


    '''
    total = sum(scores)
    # 학생들의 평균을 사용한다.
    average = sum(scores)/len(scores)
    maximum = max(scores)
    minimum = min(scores)

    return total,average,maximum,minimum

total, average, maximum, minimum = analyze_scores(scores)

print("합계:", total)
print("합계:", average)
print("합계:", maximum)
print("합계:", minimum)

# help(analyze_scores)
print(analyze_scores.__doc__)