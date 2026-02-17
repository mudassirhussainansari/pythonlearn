students = {}

for i in range(3):
    name = input("Enter the student name: ")
    marks = int(input("Enter your marks: "))
    students[name] = marks

print("Student data: ", students)

highest_student_marks = max(students, key=students.get)
print("Highest student marks: ",highest_student_marks)

average = sum(students.values()) / len(students)
print("Average student is: ",average)

for name, marks in students.items():
    if marks > 75:
        print(name,"-", marks)
    
