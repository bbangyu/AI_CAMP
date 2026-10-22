print("="*50)
print("연산자 우선 순위")
print("="*50)

result = 10 + 2 * 3

print(f'result:{result}')

result = (10 + 2) * 3
print(f'result:{result}')

print(20 / 5 + 3) # 7.0
print(2 ** 3 + 2) # 10
print(10+5 > 12)  # True
print(10 > 5 and 20 > 10)
print(True or False and False) #True

# 문제 1
print(5 + 3 * 2) #11

# 문제 2
print((5 + 3) * 2) #16

# 문제 3
print(20 // 3 + 2) #8

# 문제 4
print(2 ** 3 * 2) #16

# 문제 5
print(10 - 2 * 3 + 5) #9

# 문제 6
print(10 + 5 >= 15) #True

# 문제 7
print(10 > 5 and 3 < 1) #False

# 문제 8
print(10 > 5 or 3 < 1) #False

# 문제 9
print(not 10 > 5) #False

# 문제 10
print((10 > 5 or 3 < 1) and 20 == 20) #True