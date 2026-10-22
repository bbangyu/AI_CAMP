
print("="*50)
print("입력과 출력 함수")
print("="*50)

print('Hello World!')
print(100)
print(3.14)

#변수 출력
name = "이상무"
age = 21

print(name)
print(age)
print("="*50)
print("1. 여러 값 출력")
print("="*50)

print("합계:", 10+20)
print("곱셈:", 10*3)

print("Python","Java","AI")

#shift + end : 라인 끝까지 선택
print("Python","Java","AI",sep="-")
print("010","1234","5678",sep="-")

print("="*50)
print("2. end로 줄바꿈 제어하기")
print("="*50)

print("A")
print("B")

print("A",end=" ")
print("B")

# ㅁ,ㅂ.. + 한자
print("01_Python",end="→")
print("02_Database",end="→")
print("03_WEB")

print("="*50)
print("3. 입력 input()")
print("="*50)

# name=input("이름을 입력하세요:")

# print("이름:",name)

# age = input("나이를 입력하세요: ")

# print("나이",age)
# print("자료형",type(age))

age = int(input("나이를 입력하세요: "))

print("현재 나이",age)
print("내년 나이",age+1)
print("자료형",type(age))