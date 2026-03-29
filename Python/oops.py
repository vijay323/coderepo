class Student:
    def __init__(self,full_name,class_grade,percentage):
        self.name=full_name
        self.grade=class_grade
        self.percentage=percentage
    def student_details(self):
        print(f"{self.name} is in Class {self.grade}")

s1=Student("Vijay", 11,99)
s1.student_details()
s1.percentage=80


s1.student_details()

del s1.percentage

s1.student_details()

print(s1.__dict__)

del s1

s1.student_details()