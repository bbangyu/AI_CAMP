# p02_simple_class_init_run.py

# 클래스 선언
class Book:

    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def show_info(self):
        print(f'도서제목: {self.title}')
        print(f'저자: {self.author}')
        print(f'가격: {self.price:,}원')
        print("="*50)

    def change_price(self, new_price):
        # 단 가격은 0원 이상
        if new_price < 0:
            print('가격은 0원 이상이어야 합니다.') 
            return
        self.price = new_price
        print("도서 가격이 변경되었습니다.")
    
        

def main():
    # 객체 생성
    book1 = Book("책1","저자1",10_000)

    print("=== 가격 변경 전 ===")
    book1.show_info()

    # 가격 변경 : 정상변경
    book1.change_price(25_000)

    print("=== 가격 변경 후 ===")
    book1.show_info()

  
    book1.change_price(-500)
    print("\n=== 최종 도서 정보 ===")
    book1.show_info()
if __name__ == "__main__":
    main()