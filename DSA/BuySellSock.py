prices = [7,1,5,3,6,4]

def Solution(prices):
    minp=prices[0]
    maxp=0

    for i in range(1,len(prices)):
        if minp>prices[i]:
            minp=prices[i]
        else:
            maxp=max(maxp,prices[i]-minp)
    return maxp

print(Solution(prices))