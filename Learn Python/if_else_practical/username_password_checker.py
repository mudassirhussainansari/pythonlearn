# username and password checker

username = input("Enter the username: ")
password = input("Enter the password: ")

if username.lower() == "admin" and password.lower() == "1234":
    print("Your are loggin successfully")
else:
    print("Invalid username and password")
