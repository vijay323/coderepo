class Vehicle:
    def __init__(self, vehicle_id, name, rent_per_day):
        self.vehicle_id = vehicle_id
        self.name = name
        self.rent_per_day = rent_per_day
        self.available = True

    def display(self):
        status = "Available" if self.available else "Not Available"
        print(f"ID: {self.vehicle_id}, Name: {self.name}, Rent/Day: {self.rent_per_day}, Status: {status}")

    def calculate_rent(self, days):
        total = self.rent_per_day * days
        if days > 5:
            total = total - (total * 0.10)
        return total

    def rent_vehicle(self):
        if self.available:
            self.available = False
            return True
        return False

    def return_vehicle(self):
        self.available = True


class Car(Vehicle):
    def __init__(self, vehicle_id, name, rent_per_day, seats, fuel_type):
        super().__init__(vehicle_id, name, rent_per_day)
        self.seats = seats
        self.fuel_type = fuel_type

    def display(self):
        status = "Available" if self.available else "Not Available"
        print(f"Car -> ID: {self.vehicle_id}, Name: {self.name}, Seats: {self.seats}, Fuel: {self.fuel_type}, Rent/Day: {self.rent_per_day}, Status: {status}")


class Bike(Vehicle):
    def __init__(self, vehicle_id, name, rent_per_day, cc):
        super().__init__(vehicle_id, name, rent_per_day)
        self.cc = cc

    def display(self):
        status = "Available" if self.available else "Not Available"
        print(f"Bike -> ID: {self.vehicle_id}, Name: {self.name}, CC: {self.cc}, Rent/Day: {self.rent_per_day}, Status: {status}")


class Customer:
    def __init__(self, customer_id, name, phone):
        self.customer_id = customer_id
        self.name = name
        self.phone = phone

    def display(self):
        print(f"Customer ID: {self.customer_id}, Name: {self.name}, Phone: {self.phone}")


class RentalSystem:
    def __init__(self):
        self.vehicles = []
        self.customers = []
        self.rental_records = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def add_customer(self, customer):
        self.customers.append(customer)

    def show_available_vehicles(self):
        found = False
        print("\nAvailable Vehicles:")
        for vehicle in self.vehicles:
            if vehicle.available:
                vehicle.display()
                found = True
        if not found:
            print("No vehicles available.")

    def show_all_vehicles(self):
        print("\nAll Vehicles:")
        for vehicle in self.vehicles:
            vehicle.display()

    def rent_vehicle(self, customer_id, vehicle_id, days):
        customer = None
        vehicle = None

        for c in self.customers:
            if c.customer_id == customer_id:
                customer = c
                break

        for v in self.vehicles:
            if v.vehicle_id == vehicle_id:
                vehicle = v
                break

        if customer is None:
            print("Customer not found.")
            return

        if vehicle is None:
            print("Vehicle not found.")
            return

        if vehicle.rent_vehicle():
            total_rent = vehicle.calculate_rent(days)
            self.rental_records.append({
                "customer_id": customer.customer_id,
                "customer_name": customer.name,
                "vehicle_id": vehicle.vehicle_id,
                "vehicle_name": vehicle.name,
                "days": days,
                "total_rent": total_rent
            })
            print(f"\nVehicle rented successfully to {customer.name}")
            print(f"Vehicle: {vehicle.name}")
            print(f"Days: {days}")
            print(f"Total Rent: {total_rent}")
            if days > 5:
                print("10% discount applied.")
        else:
            print("Vehicle is already rented.")

    def return_vehicle(self, vehicle_id):
        for vehicle in self.vehicles:
            if vehicle.vehicle_id == vehicle_id:
                if vehicle.available:
                    print("This vehicle is already available.")
                else:
                    vehicle.return_vehicle()
                    print(f"{vehicle.name} returned successfully.")
                return
        print("Vehicle not found.")

    def show_rental_history(self):
        print("\nRental History:")
        if not self.rental_records:
            print("No rental records found.")
        else:
            for record in self.rental_records:
                print(f"Customer: {record['customer_name']}, Vehicle: {record['vehicle_name']}, Days: {record['days']}, Total Rent: {record['total_rent']}")


system = RentalSystem()

system.add_vehicle(Car("C101", "Swift", 1500, 5, "Petrol"))
system.add_vehicle(Car("C102", "Creta", 2500, 5, "Diesel"))
system.add_vehicle(Bike("B101", "Pulsar", 500, 150))
system.add_vehicle(Bike("B102", "Activa", 400, 110))

system.add_customer(Customer("CU1", "Shristi", "9876543210"))
system.add_customer(Customer("CU2", "Rahul", "9123456780"))

while True:
    print("\n===== Vehicle Rental System =====")
    print("1. Show Available Vehicles")
    print("2. Show All Vehicles")
    print("3. Rent Vehicle")
    print("4. Return Vehicle")
    print("5. Show Rental History")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        system.show_available_vehicles()

    elif choice == 2:
        system.show_all_vehicles()

    elif choice == 3:
        customer_id = input("Enter Customer ID: ")
        vehicle_id = input("Enter Vehicle ID: ")
        days = int(input("Enter number of days: "))
        system.rent_vehicle(customer_id, vehicle_id, days)

    elif choice == 4:
        vehicle_id = input("Enter Vehicle ID to return: ")
        system.return_vehicle(vehicle_id)

    elif choice == 5:
        system.show_rental_history()

    elif choice == 6:
        print("Thank you for using Vehicle Rental System.")
        break

    else:
        print("Invalid choice.")