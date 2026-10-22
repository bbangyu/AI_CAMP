print("="*50)
print(" 5. 요소 삭제 문제")
print("="*50)

nums = [1, 2, 3, 4, 5, 3]

# ① 값 3 하나만 삭제
nums.remove(3)
print(f'nums: {nums}')
# ② 인덱스 2 삭제
nums.pop(2)
print(f'nums: {nums}')
# ③ 마지막 값 삭제
nums.pop(-1)
print(f'nums: {nums}')
