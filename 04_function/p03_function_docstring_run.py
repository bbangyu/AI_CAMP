print("="*50)
print("Docstring")
print("="*50)

def hello(name):
    """
    화면에 인사말을 출력하는 함수 입니다.

    Args:
        name (str) : 사용자 이름

    """
    print(name,"님 안녕하세요")

hello("이상무")



def add(a,b):
    """
    두 숫자를 더한 결과를 반환합니다.
    Args:
        a(int): 첫 번째 숫자
        b(int): 두 번째 숫자  

    Returns:
        int: 두 숫자의 합
             
    """


    return a+b

add(15,3)


def divide(a,b):
    """
    두 숫자를 나눈 결과를 반환합니다.
    
    Args:
        a (float): 나누어 지는 수
        b (float): 나누는 수
        
    Return:
        float: 나눗셈 결과
        
    Raises:
        ZeroDivisionError: b가 0인 경우
    """

    return a/b

print(divide(10,0))