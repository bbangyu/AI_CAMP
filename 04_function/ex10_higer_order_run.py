print("="*50)
print("3. 회원 등급에 따른 할인 정책 적용")
print("="*50)

def normal_discount(price):
		# 할인 없음
        return price

def gold_discount(price):
		# 10% 할인
        return price*0.9

def vip_discount(price):
		# 20% 할인
        return price*0.8
def calculate_price(price, discount_func):
        # 전달 받은 함수 실행
        return discount_func(price)

result_normal=calculate_price(100_000,normal_discount)
print(f'result_normal:{result_normal:,}')
print(calculate_price(100_000, gold_discount))
print(calculate_price(100_000, vip_discount))