# p03_oop_bank_account.py

class BankAccount:

    # 생성자
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    # 입금 메서드
    def deposit(self, amount):
        self.balance += amount

    # 출금 메서드
    def withdraw(self, amount):
        if amount > self.balance:
            print("잔액이 부족합니다.")
            return

        self.balance -= amount

    # 잔액 조회 메서드
    def show_balance(self):
        print(f"예금주: {self.owner}")
        print(f"현재 잔액: {self.balance}")


def main():
    # 객체 생성
    account = BankAccount("이상무", 100_000)

    # 메서드 호출
    account.deposit(50_000)
    account.withdraw(30_000)

    account.show_balance()


if __name__ == "__main__":
    main()