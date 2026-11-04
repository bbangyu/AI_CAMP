try:
	number = int(input("숫자를 입력하세요:"))

	result = 10 / number


except ZeroDivisionError:
	print("0으로 나눌 수 없습니다.")

print("프로그램 종료!")
	