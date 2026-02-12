# wap to check the input user is even or odd

value = int(input("Enter your number: "))

if (value>0):
    if (value%2==0):
        print("Enter value is Even")
    else:
        print("Enter value is Odd")
else:
    print("Enter the valid value")





# wap to find the largest of three numbers

first_number = int(input("Enter your number: "))
second_number = int(input("Enter your number: "))
third_number = int(input("Enter your number: "))

if (first_number > second_number or first_number> third_number):
    print(first_number)
elif (second_number > first_number and second_number > third_number):
    print(second_number)
else:
    print(third_number)


# wap to check number is multiple of 7 or not
value = int(input("Enter the number:" ))
if (value%7==0):
    print("The number is multiple of 7")
else:
    print("The number is not multiple of 7")





