try:
	number = int(input("숫자를 입력하세요:"))

	result = 10 / number
	print("result:", result)

except ValueError:
	print("숫자만 입력해야 합니다.")

except ZeroDivisionError:
	print("0으로 나눌 수 없습니다.")

print("프로그램 종료!")
	