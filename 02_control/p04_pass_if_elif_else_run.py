print("="*50)
print("성적을 입력 받아 출력")
print("="*50)

score = int(input('성적을 입력 하세요: '))

print(f'score:{score}')

if score >=90:
    print('A 학점')
elif score >= 80:
    pass
elif score >= 70:
    print('C학점')
elif score >= 60:
    print('D학점')
else:
    print('F학점')