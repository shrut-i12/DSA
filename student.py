student={}
n= int(input("enter number of student:"))
for i in range(n):
    rollno=input("enter the rollnumber:")
    name=input("enter the name:")
    student[rollno]=name
print("student details:")
for rollno,name in student.items():
    print("Rollno:",rollno,"Name:",name) 