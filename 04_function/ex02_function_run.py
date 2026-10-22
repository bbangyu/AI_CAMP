print("="*50)
print("2. 회원 등급 판정 함수")
print("="*50)

### 2. 회원 등급 판정 함수

# 회원 이름과 구매 금액을 전달 받아 회원 등급을 반환하는 get_grade() 함수를 작성하세요.

name = "Kim"
price = 750_000

def get_grade(price):
    grade = "";

    if price >= 1_000_000:
        grade = "VIP"
    elif price >= 500_000:
        grade = "GOLD"
    elif price >= 100_000:
        grade = "SILVER"
    else:
        grade = "NORMAL"

    return grade

grade = get_grade(price)

print(name, "회원등급:",grade)