class Payment:

    def __init__(self, amount):
        self.amount = amount

    def pay(self):
        print("Processing payment...")


class UPI(Payment):

    def pay(self):
        print(f"Paid rs{self.amount} using UPI")


class Card(Payment):4 saASDTYUIOP]\ 

    def pay(self):
        print(f"Paid rs{self.amount} using Card")


class NetBanking(Payment):

    def pay(self):
        print(f"Paid rs{self.amount} using Net Banking")


# usage
p1 = UPI(1000)
p2 = Card(2000)
p3 = NetBanking(3000)

p1.pay()
p2.pay()
p3.pay()