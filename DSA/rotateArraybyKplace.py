def Reverse(nums,l,r):
    while l<r:
        nums[l],nums[r]=nums[r],nums[l]
        l+=1
        r-=1
    

def Rotate(num,n,k):
    k=k%n
    Reverse(num,n-k,n-1)
    Reverse(num,0,n-k-1)
    Reverse(num,0,n-1)


nums=[23,21,3,4,1,63,2]

Rotate(nums,len(nums),3)

print(nums)