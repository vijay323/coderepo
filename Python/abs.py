from abc import ABC, abstractmethod

# class Animal(ABC):

#     @abstractmethod
#     def sound(self):
#         pass

# class Dog(Animal):

#     def sound(self):
#         print("Dog Barks")

# class Cat(Animal):

#     def sound(self):
#         print("Cat meows")

# d=Dog()
# d.sound()

# c=Cat()
# c.sound()


class Payment(ABC):

    @abstractmethod
    def pay(self,amount):
        pass

class UPI(Payment):

    def pay(self,amount):
        print(f"RS {amount} paid using UPI!")

class Card(Payment):

    def pay(self,amount):
        print(f"RS {amount} paid using CARD!")

u=UPI()

u.pay(6064)

c=Card()
c.pay(6549055)