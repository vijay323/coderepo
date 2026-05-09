def SubMax(arr,k):
    s=0
    n=len(arr)
    s_max=0
    for i in range(0,n-k+1):
        s+=arr[j]
        s_max=max(s,s_max)
    return s_max

print(SubMax([2, 3, 4, 1, 5], 2))
