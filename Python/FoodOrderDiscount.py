class DiscountStrategy:
    def apply_discount(self, amount):
        return amount

class NoDiscount(DiscountStrategy):
    def apply_discount(self, amount):
        return amount

class FestivalDiscount(DiscountStrategy):
    def apply_discount(self, amount):
        return amount - (amount * 10 / 100)

class PremiumUserDiscount(DiscountStrategy):
    def apply_discount(self, amount):
        return amount - (amount * 20 / 100)

def final_bill(strategy, amount):
    payable = strategy.apply_discount(amount)
    print(f"Original Amount: ₹{amount}")
    print(f"Final Amount: ₹{payable}")

final_bill(NoDiscount(), 1000)
print()

final_bill(FestivalDiscount(), 1000)
print()

final_bill(PremiumUserDiscount(), 1000)