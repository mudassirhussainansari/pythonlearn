import random
import string


pass_len = int(input("Enter the password length: "))
generate_password = ""

upper_letter = string.ascii_uppercase
lower_letter = string.ascii_lowercase
digits = string.digits
special_character = string.punctuation
string_char = string.ascii_letters + string.digits + string.punctuation

choice = int(input("please select you password is only \n 1. upper letter \n 2. lower letter \n 3. digit \n 4. special character \n 5. mix \n"))

if (choice == 1):
    for i in range(pass_len):
        generate_password += random.choice(upper_letter)
elif (choice == 2):
    for i in range(pass_len):
        generate_password += random.choice(lower_letter)
elif (choice == 3):
    for i in range(pass_len):
        generate_password += random.choice(digits)
elif (choice == 4):
    for i in range(pass_len):
        generate_password += random.choice(special_character)
elif (choice == 5):
    for i in range(pass_len):
        generate_password += random.choice(string_char)
else:
    print("Please enter the valid choice like 1 to 4")
    
print("Your random password -->",generate_password)