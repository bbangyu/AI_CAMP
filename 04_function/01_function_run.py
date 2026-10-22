print("="*50)
print("함수(Function)")
print("="*50)

def print_score(score):
    print("학생 점수:", score)


print_score(90)
print_score(80)
print_score(95)

print("="*50)
print("1. 함수의 정의와 호출")
print("="*50)

def hello():
    print("Hello Python")

hello()
hello()

print("="*50)
print("2. 매개변수(Parameter)")
print("="*50)

def hello(name):
    print('안녕하세요.',name)

hello('아상무')
hello('')

print("="*50)
print("3. 여러 개의 매개변수")
print("="*50)

def add(a, b):
	print(a+b)
		
add(10,20)

print("="*50)
print("4. return으로 결과 반환")
print("="*50)

def add_new(a,b):
    ''' 두 수의 합 반환'''
    result = a + b
    return result

value = add_new(15,3)

print(value)

print("="*50)
print("4.1 여러 값 반환")
print("="*50)

def calculate (a,b):
     total = a + b
     multiply = a * b

     return total, multiply

add_result, multiply_result = calculate(10,20)

print(add_result, multiply_result)
print(type(add_result))

print("="*50)
print("5. 위치 인자(Positional Arguement)")
print("="*50)

def introduce(name, age):
    print('이름:',name)	
    print('나이:',age)

introduce('PCWK',22)

print("="*50)
print("6.  키워드 인자(Keyword Argument)")
print("="*50)

introduce(name='PCWK',age=21)
introduce(age=21, name='PCWK')

print("="*50)
print("7. 기본값 매개변수(Default Parameter)")
print("="*50)

def greet(name, message='안녕하세요'):
	print(name, message)
		
greet("PCWK")
greet("PCWK",'반갑습니다.')
#키워드 인자로 전달해도 됩니다.
greet("PCWK",message='좋은 아침입니다.')

print("="*50)
print("8. *args : 위치 가변 인자")
print("="*50)

# def add_args(*args):
#      print(args)
#      print(type(args))

# add_args(15,17,20)
# add_args()

def add_new(*numbers):
     return sum(numbers)

print(add_new(10,20)         )
print(add_new(10,20,30)      )
print(add_new(10,20,30,40,50))

#일반 개개변수와 *args
print("="*50)
print("9. 일반 개개변수와 *args")
print("="*50)

def student(name, *scores):
     print("이름:",name)
     print('점수:',scores)

student("Kim",90,80,95)

print("="*50)
print("10. 일반 개개변수와 *args")
print("="*50)

def student_average(name, *scores):
     average = sum(scores) / len(scores)

     return name, average

name, average = student_average('Kim',80,90,100)

print("이름:",name)
print("평균:",average)

print("="*50)
print("11. **kwargs : 키워드 가변 인자")
print("="*50)

# def user_info(**kwargs):
# 		print(kwargs)
# 		print(type(kwargs))
		
def user_info(**kwargs):
     for key,value in kwargs.items():
          print(key, ":",value)


user_info(name="Kim", age=21, grade="VIP");

print("="*50)
print("12. *args와 **kwargs 함께 사용")
print("="*50)

def user_info(name, *scores, **kwargs):
     print("이름:",name)
     print('점수:',scores)
     print('추가정보:',kwargs)

user_info("Kim",
          80,90,100,
          age=21,
          grade='VIP'
          )