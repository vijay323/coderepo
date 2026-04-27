nums=[33,613,61,64,93,462,13]
nums.sort()
def check(arr):
    for i in range(0,len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
    return True

print(check(nums))