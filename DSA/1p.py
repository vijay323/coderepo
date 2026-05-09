nums=[5,3,2,2,1,5,5,7,5,10]
m=[10,111,1,9,5,6,7,2]

freq={}

for i in range(0,len(nums)):
    if nums[i] in freq:
        freq[nums[i]]+=1
    else:
        freq[nums[i]]=1

print(freq)






#hash_list=[0]*11
# for num in n:
#     hash_list[num]+=1

# for num in m:
#     if num<0 or num>10:
#         print("NA") 
#     else:
#         print(hash_list[num])