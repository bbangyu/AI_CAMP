

def total(*scores):
    """점수를 반환합니다.
    """
    return sum(scores)

def average(*scores):
    """평균을 반환합니다.
    """

    return sum(scores)/len(scores)

if __name__ == '__main__':
    #scores = (80, 90, 100)
    print(total(80, 90, 100))
    print(average(80, 90, 100))