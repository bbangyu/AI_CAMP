class Book:

    publisher = "PCWK 출판사"
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def show_title(self):
        print(f"제목: {self.title}")

    def show_author(self):
        print(f"저자: {self.author}")

    def show_price(self):
        print(f"가격: {self.price}")      

    def show_info(self):
        self.show_title()
        self.show_author()
        self.show_price()
        print("-"*20)

    @classmethod
    def get_publisher(cls):
        return cls.publisher

    @classmethod
    def change_publisher(cls, new_name):
        if not new_name.strip():
            #print("회사명은 필수 입니다.")
            raise ValueError("회사명은 필수 입니다.")

        cls.publisher = new_name
        



def main():
    
    book1 = Book("제목1","저자1",10_000)


    book1.show_info()

    print("변경전:",Book.get_publisher())

    #출판사명 변경
    Book.change_publisher("PCWK IT 출판사")

    print("변경후:",Book.get_publisher())
    


if __name__ == "__main__":
    main()