# f=open('hello.txt','r')
# s=f.read(10)
# print(s)
# f.close()

with open('sample.txt','a') as f:
    f.write("With context")