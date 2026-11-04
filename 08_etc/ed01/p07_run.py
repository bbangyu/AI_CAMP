def validate_age(age:int) ->None:
    if age < 0:
        raise ValueError("나이는 음수일 수 없습니다.")

    if age > 150:
        raise ValueError("나이가 허용 범위를 초과했습니다.")

try:
    validate_age(-10)
except ValueError as e:
    print("검증 실패:", e)

print("프로그램 종료")
