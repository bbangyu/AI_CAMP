print("="*50)
print("2. 조건 함수를 이용한 데이터 필터링")
print("="*50)

numbers = [10, 25, 30, 55, 60, 75, 80]

#is_even(): 짝수이면 True, 그렇지 않으면 False
def is_even(number):
    """
    짝수 판별 함수
    Args:
        number (int) 숫자 입력
        
    Return:
        짝수이면 True 그렇지 않으면 False
    """
    return number % 2 == 0

#is_over_50() : 50이상 이면 True 그렇지 않으면 False Return
def is_over_50(number):
    return number >= 50

print(list(filter(is_even,numbers)))
print(list(filter(is_over_50,numbers)))

#print(filter_data(numbers, is_even))
#print(filter_data(numbers, is_over_50))
