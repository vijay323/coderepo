def f(i,n):
    if i>n:
        return
    f(i+1,n)
    print(i)

n=int(input())
f(1,n)