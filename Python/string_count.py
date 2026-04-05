f = open('string_txt.txt')
s = f.read()
# print(s)
word_list = ['alice', 'wonder', 'natural']
print(s.find(word_list[0]))
f.close()