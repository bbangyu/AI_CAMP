print("="*50)
print(" 7. 리스트 응용(리스트 컴프리헨션)")
print("="*50)

nums = [1, 2, 3, 4, 5, 6, 7, 8]
print(f"원본: {nums}")
# ① 홀수만 추출
# for num in nums:
#     if num % 2 != 0:
#         print(num,end=" ")

# 리스트 컴프리헨션
odds = [num for num in nums if num % 2 !=0]
print(odds)

# ② 각 요소의 제곱값 리스트 작성
# xx = []
# for num in nums:
#     xx.append(num**2)

# print(f'\nnums: {nums}')
# print(f'xx: {xx}')

# 리스트 컴프리헨션
squares = [i**2 for i in nums]
print(squares)