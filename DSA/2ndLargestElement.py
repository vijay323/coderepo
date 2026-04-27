nums=[23,26,1,8,3,49,63,4,74,23,6]

def sec_Largest(arr):
    largest=float("-inf")
    s_largest=float("-inf")

    for i in range(0,len(arr)):
        if arr[i]>largest:
            s_largest=largest
            largest=arr[i]
        elif arr[i]>s_largest and arr[i]!=largest:
            s_largest=arr[i]
        
    return s_largest

print(sec_Largest(nums))