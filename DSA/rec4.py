def nsum(i,sum):
    if i==0:
        print(sum)
        return
    nsum(i-1,sum+i)

n=int(input())
nsum(n,0)    