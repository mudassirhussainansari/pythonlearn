"""Write a Python program that:

Takes marks of 5 students as input.

Stores them in a list.

Prints:

Total marks

Average marks

Highest marks

Lowest marks"""

marks_list = []

marks = int(input("Enter the 1st marks: "))
marks_list.append(marks)

marks = int(input("Enter the 2nd marks: "))
marks_list.append(marks)

marks = int(input("Enter the 3rd marks: "))
marks_list.append(marks)

marks = int(input("Enter the 4th marks: "))
marks_list.append(marks)

marks = int(input("Enter the 5th marks: "))
marks_list.append(marks)

print(marks_list)  # first solution

total_marks = 0

for marks in marks_list:
    total_marks += marks


print(total_marks) #second solution

print(total_marks // 5)

marks_list.sort()

print(marks_list[-1])

print(marks_list[0])

