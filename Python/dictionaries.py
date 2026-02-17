d1={1:"Geeks",2:"For",3:"Geeks"}
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

