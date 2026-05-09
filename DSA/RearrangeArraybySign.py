nums=[3,1,-2,-5,2,-4]

def Solution(nums):
    pos,neg=0,1
    res=[0]*len(nums)
    for i in range(len(nums)):
        if nums[i]>0:
            res[pos]=nums[i]
            pos+=2
        else:
            res[neg]=nums[i]
            neg+=2
    return res

print(Solution(nums))