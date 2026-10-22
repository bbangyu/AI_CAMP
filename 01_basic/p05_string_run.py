# p05_string_run.py

#1. 문자열 선언

print("="*50)
print("01. 문자열 선언")
print("="*50)

name     = "이상무"
language = 'Python'
message  = """ Hello Python """

print("이름:",name)
print("학습언어:",language)
print("자료형:",type(language))
print(message)

message = "I'm learning Python."
print(message) 

message = '그는 "Python"을 공부합니다.'
print(message)

print("="*50)
print("02. 이스케이프 문자")
print("="*50)

print('Python\nJava')
print('이름\t나이')
print('이상무\t21')
print("C:\\AI_CAMP_20260921\\01_PYTHON\\WORKSPACE")

message = '그는 \"Python\"을 공부합니다.'
print(message)

print("="*50)
print("03. 문자열 연결하기")
print("="*50)

first_name = "상무"
last_name  = "이"

name = last_name + first_name 

print(name)

language = "Python"
message  = "나는 " +language+"을 공부합니다."
print(message)

age = 21
print("나이: "+str(age))

print("="*50)
print("04. 문자열 반복하기")
print("="*50)

message = 'Python '
print(message * 3)

print("="*50)
print("05. 문자열 길이 확인하기")
print("="*50)

language = 'Python'
print(len(language))

name = '이상무'
print(len(name))

print("="*50)
print("06. 문자열 인덱싱")
print("="*50)

language = 'Python'

print(language[0])
print(language[1])
print(language[-1])

print("="*50)
print("07. 문자열 슬라이싱")
print("="*50)

language = 'Python'
print(language[0:2]) #Py
print(language[2:6]) #thon
print(language[:3])  #Pyt
print(language[3:])  #hon

