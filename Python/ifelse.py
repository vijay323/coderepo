# x=int(input("Enter an  integer: "))

# if x>5:
#     print("Greater than 5")
# elif x==5:
#     print("Equals to 5")
# else:
#     print("Smaller than 5")

# year=int(input("enter a year: "))

# if (year%4==0 and year%100!=0) or year%400==0:
#     print("Its a leap year")
# else:
#     print("not a leap year")

a,b,c=map(int,input("Enter 3 number: ").split())

if a==b==c:
    print("All the numbers are equal")
elif a>=b and a>=c:
    print("a is greater")
elif b>=a and b>=c:
    print("b is greater")
else:
    print("c is greater")