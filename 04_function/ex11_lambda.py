#최종 가격 = 가격 * (1- 할인율)
discount = lambda price, rate: price * (1 - rate)
                                        

print(discount(100000, 0.1))
print(discount(200000, 0.2))