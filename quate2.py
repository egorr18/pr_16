from abc import ABC, abstractmethod

# обробки платежів
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

# кредитна картка
class CreditCardPayment(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")

# PayPal
class PayPalPayment(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")

# криптовалюти
class CryptoPayment(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing cryptocurrency payment of ${amount}")

# Apple Pay
class ApplePayPayment(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing Apple Pay payment of ${amount}")

# приймає будь-який тип платежу
class PaymentHandler:
    def __init__(self, processor: PaymentProcessor):
        self.processor = processor

    def handle_payment(self, amount):
        self.processor.process_payment(amount)

if __name__ == "__main__":
    payments = [
        CreditCardPayment(),
        PayPalPayment(),
        CryptoPayment(),
        ApplePayPayment()
    ]

    for payment in payments:
        handler = PaymentHandler(payment)
        handler.handle_payment(100)
