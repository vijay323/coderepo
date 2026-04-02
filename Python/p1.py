class UPI:
    def pay(self, amount):
        print(f"Paid {amount} using UPI")

class Card:
    def pay(self, amount):
        print(f"Paid {amount} using Card")

class Wallet:
    def pay(self, amount):
        print(f"Paid {amount} using Wallet")

u1 = UPI()
c1 = Card()
w1 = Wallet()

u1.pay(500)
c1.pay(500)
w1.pay(500)