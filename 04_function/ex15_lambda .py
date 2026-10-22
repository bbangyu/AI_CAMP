print("="*50)
print("5. 상품 가격을 기준으로 정렬하기")
print("="*50)


products = [
    {"name": "노트북", "price": 1500000},
    {"name": "마우스", "price": 30000},
    {"name": "키보드", "price": 120000},
    {"name": "모니터", "price": 350000}
]

result = sorted(
    products,
    key=lambda product: product['price'],
    reverse=True
)

for product in result:
    print(product['name'],product.get('price',0))

