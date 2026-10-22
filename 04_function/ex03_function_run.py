print("="*50)
print("3. 상품 할인 가격 계산")
print("="*50)

# ### 3. 상품 할인 가격 계산

# 상품 가격과 할인율을  전달 받아 최종 가격을 계산하는 calculate_price()함수를 작성하세요.
# 할인율의 기본값은 10%로 설정합니다.
# 최종가격 = 가격 * (1 - 할인율)

# calculate_price()

def calculate_price(price, rate=0.1):
    final_price = price * (1-rate)
    discount    = price - final_price
    print(f'final_price:{final_price}')
    print(f'discount:{discount}')

    return discount, final_price

discount, final_price = calculate_price(100_000,0.2)

print(f'할인금액:{discount}')
print(f'최종금액:{final_price}')