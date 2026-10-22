print("="*50)
print("01.문자열 내장 함수와 메서드")
print("="*50)

text = 'Python'

print(len(text))      #내장 함수
print(text.upper())   #문자열 메서드 : 대문자
print(text.lower())   #문자열 메서드 : 소문자

text = "   Python   "
print(f"|{text}|")
print(f"|{text.strip()}|")

#### 1stripn() : 왼쪽 공백 제거
#### rstrip() : 오른쪽 공백 제거
print(f'|{text.lstrip()}|')
print(f'|{text.rstrip()}|')

#### replace() - 문자열 변경
text = "I like Java"
result = text.replace("Java", "Python")

print(result)
print(text)

#### find() - 문자열 찾기
text = "Hello Python"
print(text.find('Python'))

#### index() - 문자열 찾기
print(text.index('Python99'))
