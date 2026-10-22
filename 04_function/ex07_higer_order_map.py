print("="*50)
print("1. 학생 점수 처리 방법 선택하기")
print("="*50)

def add_bonus(score):
    return score + 5
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
    
scores = [95,80,70,60]
#process_scores 작성
def process_scores(scores, func):
    result = []

    for score in scores:
        #print(func(score))
        result.append(func(score))

    return result
    
print(list(map(add_bonus,scores)))
print(list(map(get_grade,scores)))