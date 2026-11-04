# p09_post_init_run.py

from dataclasses import dataclass, field

@dataclass
class Product:
    name:str
    price:int
    quantity:int
    total:int = field(init=False)

    def __post_init__(self):
        if self.price < 0 or self.quantity < 0:
            raise ValueError("가격과 수량은 음수일 수 없습니다.")

        self.total = self.price * self.quantity

product =  Product("키보드",50_000,2) 

print(product)
print(product.total)