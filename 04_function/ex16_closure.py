print("="*50)
print("1. 은행 계좌 잔액 관리")
print("="*50)



def create_account(balance):

    def deposit(amount):
        nonlocal balance
        balance += amount
        return balance

    return deposit


account=create_account(10_000)


print(account(5000))
print(account(3000))
print(account(2000))