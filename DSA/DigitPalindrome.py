num=int(input())

n=num
r=0
while n>0:
    ld=n%10
    r=r*10+ld
    n=n//10

if r==num:
    print("Palindrome")
else:
    print("Not a Palindrome")