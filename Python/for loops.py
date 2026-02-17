n=int(input("Enter a integer ="))

'''for i in range(1,11):
    print(f"{n} x ",i,"=",n*i)'''
fact=1
for i in range(1,n+1):
    fact=fact*i

print(fact)
