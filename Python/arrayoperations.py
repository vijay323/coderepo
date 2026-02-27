from numpy import *

arr1=array([8,22,2254,5,542,5])
arr2=array([5,25,124,44,2,1])

# arr=arr2 + arr1
# print(arr)

print(sum(arr1))

print(min(arr1))

print(sort(arr1))

print(concatenate([arr1,arr2]))

arr1=arr2

print(arr1)

arr=arr1.view()
print(arr)

arr=arr2.copy()