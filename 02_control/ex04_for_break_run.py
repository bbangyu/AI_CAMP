print("="*50)
print("1~10에서 3의 배수만 건너뛰기.")
print("="*50)

for i in range(1,11):
    if i % 3 ==0:
        continue

    print(i,end=" ")

print("")
print("="*50)
print("2. 문자열에서 특정 문자 찾기")
print("="*50)

mail = "jamesol@naver.com"
for ch in mail:
    if '@'==ch:
        print('@ 문자를 찾았습니다.')
        break

    print(ch,end="")