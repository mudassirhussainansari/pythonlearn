# Find smallest of 3 numbers

first_num = int(input("Enter the number: "))
second_num = int(input("Enter the number: "))
third_num = int(input("Enter the number: "))

if first_num <= second_num and first_num <= third_num:
    print("first number is smallest:",first_num)
elif second_num <= first_num and second_num <= third_num:
    print("second number is smallest:",second_num)
else:
    print("third number is smallest:",third_num)
