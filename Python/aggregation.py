class Customer:

    def __init__(self,name,age,address):
        self.name= name
        self.age= age
        self.address=address

    def print_details(self):
        print(self.name,self.age,self.address.city,self.address.state,self.address.pin)

    def edit_profile(self,new_name,new_age,new_city,new_state,new_pin):
        self.name=new_name
        self.age=new_age
        self.address.edit_address(new_city,new_state,new_pin)


class Address:

    def __init__(self,city,state,pin):
        self.city=city
        self.state=state
        self.pin=pin

    def edit_address(self,new_city,new_state,new_pin):
        self.city=new_city
        self.state=new_state
        self.pin=new_pin

add=Address("Angul","Odisha",759122)
cust=Customer('Vijay',23,add)

cust.print_details()
cust.edit_profile('Rakesh',22,'Bhubaneswar','odisha',795996)
cust.print_details()