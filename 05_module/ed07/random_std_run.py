import random

#a이상 b이하의 임의의 정수(int) 반환 합니다.
number = random.randint(1,10)

#0.0이상 1.0 미만의 임의의 실수(Float)를 반환합니다.
num_float = random.random()

print(f'생성된 숫자: {number}')
print(f'num_flaot: {num_float}')