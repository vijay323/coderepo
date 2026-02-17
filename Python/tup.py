# tup = ('Geeks')
# n = 5
# for i in range(int(n)):
#     tup = (tup,)
#     print(tup)

t = (1, [2, 3])
t[1][0] = 100   # Allowed
print(t)