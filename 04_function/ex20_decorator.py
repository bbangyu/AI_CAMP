print("="*50)
print("2. 함수 반환값을 두 배로 만들기")
print("="*50)

def double_result(func):
    def wrapper(*args,**kwargs):
        for i in args:print(i)
        result = func(*args, **kwargs)
        return result * 2 
    return wrapper
	

@double_result
def add(a, b):
	return a + b
		
print(add(a=10,b=20))
print(add(5,15))