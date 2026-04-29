def Solution(nums,k):
    sum=k
    
    for i in range(0,len(nums)-1):
        j=i+1
        if nums[i]+nums[j]!=sum:
            j+=1
        else:
            return nums[i,j]
        

nums=[5,9,1,2,4,15,6,3]
k=13
print(Solution(nums,k))
