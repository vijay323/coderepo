c=0
n=int(input())
s=input("Enter Name")
def rec(s,n):
    global c
    if c==n:
        return
    else:
        print(s)
        c+=1
        rec(s,n)

rec(s,n)