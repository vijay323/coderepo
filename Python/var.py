# age=int(input("Enter your age:= "))
# name=input("Enter your name:= ")
# marks=float(input("Enter your marks:= "))

# print(f"Age= {age}, Name= {name}, Marks= {marks} ")

def nonNegativeAverage(arr):
    
    #Write your code to find average of positive numbers in number list
    #Return the answer
    x=0
    count=0
    for i in arr:
        if i>=0:
            x+=i
            count+=1
    print(x/count)
            

nonNegativeAverage([-12, 8, -7, 6, 12, -9, 14])