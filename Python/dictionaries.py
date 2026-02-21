d1={1:"Geeks",2:"For",3:"Geeks",4:"Vijay",5:"Jay"}
print(d1)

print(d1.get(1))

print(d1[2])

d1["age"]=22
print(d1)

d1[1]="Geek"
print( d1)

del d1[1]
print(d1)

val=d1.pop(3)
print(val)

key,value=d1.popitem()
print(key,value)

for key in d1:
    print(key)

d2={3:"AJAY",6:"RAJ"}

for values in d2.values():
    print(values)

for key,values in d2.items():
    print(f"{key}:{values}")