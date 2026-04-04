# f=open('sample.txt','w')
# f.write('hello world')
# f.close

# f=open('Hello.txt','w')
# f.write('Hello \nNEw line')
# f.write('\nHow are you')
# f.close()

# f=open('sample.txt','a')
# f.write('Appended this line')
# f.close()

L=['Hello\n','Hi\n','How are you\n']

f=open('hello.txt','w')
f.writelines(L)
f.close()