from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def book_ticket(self, passenger, distance):
        pass

class Bus(Transport):
    def book_ticket(self, passenger, distance):
        fare = distance * 3
        print(f"Bus Ticket Booked for {passenger} | Fare: ₹{fare}")

class Train(Transport):
    def book_ticket(self, passenger, distance):
        fare = distance * 2
        print(f"Train Ticket Booked for {passenger} | Fare: ₹{fare}")

class Flight(Transport):
    def book_ticket(self, passenger, distance):
        fare = distance * 8
        print(f"Flight Ticket Booked for {passenger} | Fare: ₹{fare}")

def confirm_booking(mode, passenger, distance):
    print("Booking in progress...")
    mode.book_ticket(passenger, distance)

modes = [Bus(), Train(), Flight()]

for m in modes:
    confirm_booking(m, "Vijay", 100)