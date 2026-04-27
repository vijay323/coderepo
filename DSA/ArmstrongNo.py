n=int(input())

num=n
l=len(num)
a=0
while(n>0):
    t=n%10
    a=a+(t**3)
    n=n//10

if a==num:
    print("Armstrong")
else:
    print("Not Armstrong")