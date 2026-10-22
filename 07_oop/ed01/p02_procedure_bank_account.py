# p02_procedure_bank_account.py

# 입금함수 
def deposit(balance,amount):
    return balance + amount

# 출금함수
def withdraw(balance,amount):
    if amount > balance:
        print('잔액이 부족합니다.')
        return balance

    return balance - amount

# 잔액 조회 함수
def show_balance(balance):
    print(f'현재 잔액: {balance:,}원')

def main():
    balance = 100_000

    balacne = deposit(balance, 50_0000)
    balance = withdraw(balance, 30_000)

    show_balance(balance)

if __name__ == "__main__":
    main()