import math
n=int(input())
i=1
lst=[]
for i in range(1,int(math.sqrt(n)+1)):
    if n%i==0:
        lst.append(i)
        if i != n//i:
            lst.append(n//i)

lst.sort()
for i in lst:
    print(i)