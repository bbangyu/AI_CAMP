

height = float(input('키(cm):'))
weight = float(input('몸무게(kg):'))

print(f'height:{height},\t type:{type(height)}')
print(f'weight:{weight},\t type:{type(weight)}')

#cm -> m 변환
height = height/100

#BMI 계산식
bmi = weight / (height ** 2)

print(f'bmi:{bmi:.2f},\t type:{type(bmi)}')

#판단
if bmi < 18.5:
    print('저체중')
elif bmi < 23:
    print('정상')
elif bmi<25:
    print('과체중')
else: 
    print('비만')