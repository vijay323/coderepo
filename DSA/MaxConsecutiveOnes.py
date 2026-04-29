def Solution(nums):
    count,ans=0,0
    for nums in nums:
        if nums==1:
            count+=1
        else:
            count=0
        ans=max(ans,count)
    
    return ans

nums=[1,0,1,1,1,0,0,1,1,1,1]
print(Solution(nums))