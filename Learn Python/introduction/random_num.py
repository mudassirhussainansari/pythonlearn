import random
import string

value = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@#$%"

def password_generate(length=6):
    character = string.ascii_letters + string.digits
    password = ""
    
    for _ in range(length):
        password += random.choice(character)
    
    return password


length = int(input("Enter your password length:"))

print("your password is "+password_generate(length))