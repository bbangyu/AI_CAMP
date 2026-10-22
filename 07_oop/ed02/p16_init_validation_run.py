# p16_init_validation_run.py

class Product:

    def __init__(self,name,price):

        if price < 0 :
            raise ValueError("상품 가격은 0원 이상이어야 합니다.")

        self.name = name
        self.price = price

    def show_info(self):
        print(f'상품명:{self.name}')
        print(f'가격 :{self.price:,}')

def main():
    product1 = Product("노트북",12_000_000)

    product1.show_info()

    try:
        product2 = Product("마우스",-500)
    except  ValueError as e:
        print("객체 생성 실패:",e)

    print("프로그램 종료!")


if __name__ == "__main__":
    main()