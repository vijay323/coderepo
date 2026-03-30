class BankAccount:

    def __init__(self,balance):
        self.__balance=balance

    def deposit(self,amount):
        self.__balance=self.__balance+amount
        print(f"rs{amount} deposited succesfully! Available balance : rs {self.__balance} ")

    def withdraw(self,amount):
        self.__balance=self.__balance-amount
        print(f"rs{amount} Withdrawl succesfull! Available balance : rs {self.__balance} ")

user=BankAccount(6000)

user.deposit(10000)

user.withdraw(6500)


