from math import *
n=int(input())

num=n
# count=0
# while num>0:
#     num=num//10
#     count+=1
    

# print(count)

def countdigits(num):
    return int(log10(abs(num))+1)

print(countdigits(num))