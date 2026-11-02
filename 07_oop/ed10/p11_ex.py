from typing import Protocol, runtime_checkable

@runtime_checkable
class PaymentMethod(Protocol):
    def pay(amount:int) -> bool: ...

# 신용카드 결제
class CreditCardPayment:
    def pay(self, amount:int) -> bool:
        print(f"[신용카드 결제]{amount:,}원 결제 완료")
        return True

# 계좌이체 결제
class BankTransferPayment:
    def pay(self, amount:int) -> bool:
        print(f"[계좌이체 결제]{amount:,}원 결제 완료")
        return True

# PaymentService
class PaymentService:
    def __init__(self, payment_method: PaymentMethod)-> None:
        self.payment_method = payment_method

    def checkout(self, amount:int) -> bool:
        # 결제 금액 0보다 큰 정수(원)
        if amount <= 0:
            raise ValueError("결제 금액은 0보다 커야 합니다.")

        print("결제를 시작합니다.")

        result = self.payment_method.pay(amount)

        print("결제 성공" if result else "결제 실패")
        return result

def main():

    payments: list[PaymentMethod] = [CreditCardPayment(), BankTransferPayment(), PaymentService(CreditCardPayment())]

    for payment in payments:
        
        if not isinstance(payment,PaymentMethod):
            continue
    
        service = PaymentService(payment)
        service.checkout(10_000)
        print("-"*30)

if __name__ == "__main__":
    main()
