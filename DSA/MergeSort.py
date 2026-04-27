def Merge_Sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2

    left_half=arr[:mid]
    right_half=arr[mid:]

    left_half=Merge_Sort(left_half)
    right_half=Merge_Sort(right_half)

    return Merge_array(left_half,right_half)


def Merge_array(left,right):
    result=[]
    i,j=0,0
    m,n=len(left),len(right)

    while i<m and j<n:
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    while i<m:
        result.append(left[i])
        i+=1
    while j<n:
        result.append(right[j])
        j+=1

    return result

arr=list(map(int, input().split()))


print(Merge_Sort(arr))
