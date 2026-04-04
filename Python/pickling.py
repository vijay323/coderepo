import pickle

class Person:
    
    def __init__(self,name,age):
        self.name=name
        self.age=age


    def display_info(self):
        print('Hi my name is',self.name,'and I am',self.age,'years old')


person=Person('Vijay',23)

with open('person.pkl','wb') as f:
    pickle.dump(person,f)



with open('person.pkl','rb') as f:
    person=pickle.load(f)
    person.display_info()

