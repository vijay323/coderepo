
f=open('sample.txt','r')
f2=open('sample1.txt','w')
while True:
    s=f.readline()
    print(s[:-1])
    s = s[:-1]
    if not s:
        break
    f2.write(s[::-1] + '\n')

f.close()
f2.close()
    