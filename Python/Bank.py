class Bank:

    def __init__(self,balance):
        self.balance=balance

    def withdraw(self,amount):
        if amount<0:
            raise Exception('amount cannot be -ve')
        if self.balance<amount:
            raise Exception('paise nahi hai tere paas')
        self.balance=self.balance-amount

obj=Bank(10000)

try:
    obj.withdraw(15000)
except Exception as e:
    print(e)
else:
    print(obj.balance)