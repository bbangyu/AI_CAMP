print("="*50)
print(" 6. 반복문 응용")
print("="*50)

nums = [2, 4, 6, 8, 10]


# ① 모든 요소의 합 구하기
total = 0

for num in nums:
    total+=num

print(f'total: {total}')
    
# ② 모든 요소를 2배로 만든 새로운 리스트 생성
double_list = []

for num in nums:
    double_list.append(num*2)

print(f'nums: {nums}')
print(f'double_list: {double_list}')

