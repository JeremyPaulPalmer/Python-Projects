from abc import ABC, abstractmethod
class retail(ABC):
    def receipt(self, amount):
        print("Your total is: ",amount)

    def payment(self, amount):
        pass

class CreditCardPayment(retail):
    def payment(self, amount):
        print('Your purchase of {} was approved.'.format(amount))

obj = CreditCardPayment()
obj.receipt("398.99")
obj.payment("398.99")
