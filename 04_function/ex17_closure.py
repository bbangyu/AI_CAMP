print("="*50)
print("2. 쇼핑몰 회원 등급별 할인 함수")
print("="*50)

def create_discount(rate):

    def discount(price):
        return price * (1 - rate)
    
    return discount

normal = create_discount(0)
gold = create_discount(0.1)
vip = create_discount(0.2)


print(normal(100_000))
print(gold(100_000))
print(vip(100_000))