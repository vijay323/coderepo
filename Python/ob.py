import json

def show_object(person):
    if isinstance(person,Person):
        return "{} {} age-> {} gender->{}".format(person.fname,person.lname,person.age,person.gender)


with open('obj.json','w') as f:
    json.dump(person,f,default=show_object)
    