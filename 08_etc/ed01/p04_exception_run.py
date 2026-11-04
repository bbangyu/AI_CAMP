try:
	number = int(input("숫자를 입력하세요:"))

	result = 10 / number
	print("result:", result)

except (ValueError, ZeroDivisionError) as e:
	print(f"입력 또는 계산 오류: {e}")



print("프로그램 종료!")
	