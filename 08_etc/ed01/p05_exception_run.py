try:
	number = int(input("숫자를 입력하세요:"))

	result = 10 / number
	print("result:", result)

except ValueError as e:
	print("예외 클래스:", type(e).__name__)
	print("예외 메시지:", e)

print("프로그램 종료!")
	