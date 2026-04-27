n=int(input())

def fibonnaci(n):

    if n<=1:
        return n
    flast=fibonnaci(n-1)
    slast=fibonnaci(n-2)
    return slast+flast

print(fibonnaci(n))