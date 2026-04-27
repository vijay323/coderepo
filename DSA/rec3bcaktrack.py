def f(i,n):
    if i<1:
        return
    f(i-1,n)
    print(i)

n=int(input())
f(n,n)