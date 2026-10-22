
def create_order(product,price,**kwargs):
    order = {
        'product':product,
        'price':price,
    }
    for key,value in kwargs.items():
        order[key] = value

    return order;


    
order= create_order(
    "노트북",
	1_200_000,
	user="Kim",
	grade="VIP",
	delivery="서울"
)

print(order)
