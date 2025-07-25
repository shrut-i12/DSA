
n = int(input("Enter number of students: "))
topper_name = ""
topper_marks = 0
for i in range(n):
    name = input("Enter name of student: ")
    marks = int(input("Enter marks: "))
    if marks > topper_marks:
        topper_marks = marks
        topper_name = name
print("\nTopper is:", topper_name)
print("Marks:", topper_marks)

