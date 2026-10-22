print("="*50)
print("1. 1~30에서 3의 배수의 합계를 출력하세요.")
print("="*50)

total = 0 #합계

for i in range(1,31):
    if i % 3 == 0:
        print(i,end=" ")
        total += i #total = total + i

print(f'\n합계:{total}')   