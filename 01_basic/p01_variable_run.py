# comment : 주석은 프로그램 코드에 설명을 작성하기 위한 문장입니다.
# 1. 변수 : 변수(variable)는 프로그램에서 데이터를 저장하고 사용하기 위해 붙이는 이름입니다 
import keyword

age    = 21
height = 176.8 
name   = 'Python'
name01 = 'Python'
message = '''Hello
Python
World
'''

user_name = "이상무"
#2name = "이상무" #문법 오류: 변수는 숫자로 시작 불가
Name = 'james'
name = "good"
# Ctrl + / : Comment
# for = 'keyword'

# 이름 = '이상무'
# 나이 = 21

# my name = 'Python'
# my-name = 'Python'
a,b,c = 1,2,3
x = y = z = 100
print("="*50)
print("01.변수 선언")
print("="*50)
print(age)
print(height)
print('name=',name)
print("name01=",name01)
print('message=',message)
print('user_name=',user_name)
#print('2name=',2name)
print('Name=',Name)
print('name=',name)
print('keyword',keyword.kwlist)
# print(이름)
# print(나이)
print(a)
print(b)
print(c)
print(x,y,z)

# 2. 자료형 확인
print("="*50)
print("02. 자료형 확인")
print("="*50)

name     = '이상무'
age      = 21
height   = 178.5
student  = True

print(type(name))
print(type(age))
print(type(height))
print(type(student))

x = 100
print(x, type(x))

x = "백"
print(x, type(x))

x = True
print(x, type(x))

# 3. 변수를 이용한 계산
print("="*50)
print("03_변수를 이용한 계산")
print("="*50)
price = 10000
quantity = 3
total_price = price * quantity

print('상품 가격',price)
print('수량     :',quantity)
print('총 금액  :',total_price)

# 4. 변수에 값 변경하기
print("="*50)
print("04_ 변수에 값 변경하기")
print("="*50)
score = 80
print(score);
scroe = 90
print(score)


# 5. 값 교환
print("="*50)
print("05_ 값 교환")
print("="*50)
a = 10;
b = 20;
print(a,b)
a,b = b,a
print(a,b)