import time

print("="*50)
print("3. 함수 실행 시간 측정하기")
print("="*50)


start = time.perf_counter()
end = time.perf_counter()


def timer(func):
	def wrapper(*args,**kwargs):
		start = time.perf_counter()
		result = func(*args,**kwargs)
		end = time.perf_counter()
        #실행 시간 : 0.01234초
		print(f'실행시간: {end-start:.4f}초')
		return result
	return wrapper


@timer
def calculate():

	total = 0
	
	for i in range(1,1000001):
		total += i
	
	return total
	
print("결과:", calculate())

print(f'start:{start}')
print(f'end:{end}')