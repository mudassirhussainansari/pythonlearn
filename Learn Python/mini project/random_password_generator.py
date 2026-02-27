import random
import string

def password_generate(pass_len, choice):
    generate_password = ""
    if (choice == 1):
        for i in range(pass_len):
            generate_password += random.choice(string.ascii_uppercase)
    elif (choice == 2):
        for i in range(pass_len):
            generate_password += random.choice(string.ascii_lowercase)
    elif (choice == 3):
        for i in range(pass_len):
            generate_password += random.choice(string.digits)
    elif (choice == 4):
        for i in range(pass_len):
            generate_password += random.choice(string.punctuation)
    elif (choice == 5):
        for i in range(pass_len):
            generate_password += random.choice(string.ascii_letters + string.digits + string.punctuation)
    else:
        print("Please enter the valid choice like 1 to 4")
    
    return generate_password


pass_len = int(input("Enter the password length: "))
choice = int(input("please select you password is only \n 1. upper letter \n 2. lower letter \n 3. digit \n 4. special character \n 5. mix \n"))

print("your password -->",password_generate(pass_len, choice))
