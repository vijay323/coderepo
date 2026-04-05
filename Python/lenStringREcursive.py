
l=0

def LenStr(s):
    if s=="":
        return 0
    else:
        
        return 1+LenStr(s[1::])

s=input()
print(LenStr(s)