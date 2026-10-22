#product.py
def discount_price(price, rate=0.1):
    """
    상품 가격 계산 모듈

    Args:
        price(int) 상품가격
        rate(float) 할인율 : defualt 10%
    
    Return:
        할인 금액(price * (1-rate))
    """
    return price * (1-rate)

if __name__ == '__main__':
    dis_price = discount_price(10_000,0.2)
    print(f'discount_price:: {dis_price:.0f}원')