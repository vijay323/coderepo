class ATM:

    def __init__(self):
        self.balance=0
        self.Validation()
    

    def Deposit(self,amount):
        self.balance+=amount
        print(f"Amount {amount} deposited successfully, Available Balance:{self.balance}")
    
    def Withdraw(self,amount):
        if amount>self.balance:
            print("Balance is low!")
        else:
            self.balance-=amount
            print(f"Amount {amount} withdrawl successful, Available balance={self.balance}")
    
    def Validation(self,OPIN=1234):
        
        PIN=int(input("Enter your ATM pin: "))
        if PIN==OPIN:
            while True:
                print("\nWelcome to ATM")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
                print("4. Exit")
                
                option=int(input("Choose Option"))
                if option==1:
                    amount=int(input("Enter the amount to deposit: "))
                    self.Deposit(amount)
                elif option==2:
                    amount=int(input("Enter the amount to withdraw: "))
                    self.Withdraw(amount)
                elif option==3:
                    print("Available Balance:",self.balance)
                elif option == 4:
                    print("Thank you for using ATM!")
                    break
                else:
                    print("Invalid option!")
        else:
             print("Wrong Pin Entered!")


a=ATM()

    


