def pn(i,n):
    if i==0:
        return
    print(i)
    pn(i-1,n)

n=int(input())
pn(n,n)