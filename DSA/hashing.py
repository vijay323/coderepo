n = int(input())
arr = list(map(int, input().split()))


hash_arr = [0] * 13

for i in range(n):
    hash_arr[arr[i]] += 1

q = int(input())

# for k in range(0,n):
#     # fetching
print(hash_arr)
   