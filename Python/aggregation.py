class Customer:

    def __init__(self,name,age,address):
        self.name= name
        self.age= age
        self.Address=address

    def print_details(self):
        print(self.name,self.age,self.Address.city,self.Address.state,self.Address.pin)

class Address:

    def __init__(self,city,state,pin):
        self.city=city
        self.state=state
        self.pin=pin

add=Address("Angul","Odisha",759122)
cust=Customer('Vijay',23,add)

cust.print_details()