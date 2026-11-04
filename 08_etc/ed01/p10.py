try:
	number = int("abc")

except ValueError:
	print("값 오류 처리")
		
except TypeError:
	print("자료형 오류 처리")

except Exception as e:
	print("기타 예외 처리", e)