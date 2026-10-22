# 문자열은 변경할 수 없다.

print("="*50)
print("01_문자열은 변경할 수 없다.")
print("="*50)

language = 'Python'

#TypeError: 'str' object does not support item assignment
# language[0] = 'J'

language = "J" + language[1:]
print(language)
print("="*50)
print("02_문자열 포맷팅")
print("="*50)

name = '이상무'
age = 21
height = 178.56

print("이름:%s"%name)
print("나이:%d"%age)
print("키:%.1f"%height)

print("이름:%s, 나이:%d, 키: %.1f"%(name,age,height))

print("="*50)
print("03_문자열 포맷팅: f-string")
print("="*50)

name = '이상무'
age = 21
print(f'이름:{name}')
print(f'나이:{age}')

print(f'이름은 {name}이고 나이는 {age}살입니다.');

price = 10_000
quantity = 3

print(f'가격: {price}원')
print(f'수량: {quantity }개')
print(f'총 금액: {price * quantity}')

##### 함수 호출
name = 'Python'
print(f'대문자: {name.upper()}')

###### 숫자 출력 형식 지정하기
pi = 3.141592
print(f'PI: {pi:.2f}')

##### 천 단위 구분
price = 1_234_567
print(f'가격: {price:,}원')

##### 천 단위 구분 + 소수점 이하 자리
price = 1_234_567.89
print(f'가격: {price:,.1f}원')

##### 정렬하기
name = "Python"

print(f"|{name:<10}|") #왼쪽 정렬
print(f"|{name:^10}|") #가운데 정렬
print(f"|{name:>10}|") #오른쪽 정렬

#### fomat함수 사용
print("이름: {}, 나이:{}".format(name,age))