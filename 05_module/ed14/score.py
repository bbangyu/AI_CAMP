# score.py에 total(*scores)와 average(*scores) 함수를 작성하세요.
#  main.py에서 score 모듈을 sc라는 별칭으로 가져와 
# 학생 세 명의 점수 70, 80, 90에 대한 
# 총점과 평균을 출력하세요.

def total(*scores):
    """합계 구하기
    """
    return sum(scores)

def average(*scores):
    """평균 구하기
    """
    return sum(scores)/len(scores)