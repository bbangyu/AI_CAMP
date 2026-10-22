print("="*50)
print("4. 우수 회원 데이터 추출하기")
print("="*50)

members = [
    {"name": "Kim", "price": 800000},
    {"name": "Lee", "price": 300000},
    {"name": "Park", "price": 1200000},
    {"name": "Choi", "price": 450000},
    {"name": "Jung", "price": 650000}
]


result = list (filter(
    lambda member : member ['price'] >= 500_000
    ,members
))

for member in result:
    print(member)

