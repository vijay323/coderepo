import numpy as np

a=np.random.randint(1,100,25)
print(a)

print(np.sort(a))


b=np.random.randint(1,100,24).reshape(6,4)
print(b)

print(np.sort(b))

print(np.sort(b,axis=0)[::-1])