print("="*50)
print("1. 전역 변수와 지역 변수")
print("="*50)

def calculate():
		number = 10
		result = number * 2
		
		print(number)
		print(result)

        
calculate()

print("="*50)
print("2. 전역 변수(Global Variable)")
print("="*50)

message = "Hello Python"

def hello():
	print(f'message: {message}')

hello()
print(message)

print("="*50)
print("3. 전역 변수와 지역 변수의 이름이 같은 경우")
print("="*50)

number = 100

def test():
	number = 200
	print('함수 내부:',number)

test()

print('함수 외부:',number)

print("="*50)
print("4. 전역 변수 읽기")
print("="*50)

tax_rate = 0.1

def calculate_tax(price):
	tax = price * tax_rate
	return tax

print(calculate_tax(100_000))

print("="*50)
print("5. 전역 변수 변경하기")
print("="*50)

count = 0

def increase():
	global count
	
	count +=1

increase()
increase()
increase()

print(count)

# total = 0

# def add(value):
# 	global total
# 	total += value

print("="*50)
print("6. 전역 변수 변경하기")
print("="*50)

def add(total,value):
	return total+value

total = 0

total = add(total,10)
total = add(total,20)

print(total)