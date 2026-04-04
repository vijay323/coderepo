import json

# L=[1,2,3,4,5]

# with open('demo.json','w') as f:
#     json.dump(L,f)

# D={'name':'VIjay', 'age':'23'}
# with open('demo1.json','w') as f:
#     json.dump(D,f)

# with open('demo1.json','r') as f:
#     print(json.load(f))

class Person:

    def __init__(self,fname,lname,age,gender):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.gender=gender


person=Person('Vijay','Kumar',23,'male')


# AS A STRING
# def show_object(person):
#     if isinstance(person,Person):
#         return "{} {} age-> {} gender->{}".format(person.fname,person.lname,person.age,person.gender)

#AS A DICT
def show_object(person):
    if isinstance(person,Person):
        return{'name':person.fname+' '+ person.lname,'age':person.age,'gender':person.gender}


with open('obj.json','w') as f:
    json.dump(person,f,default=show_object,indent=4)



    