# palindrome or not

name = input("Enter your name: ").lower()
# print("your reverse name", name[::-1])

if (name == name[::-1]):
    print("Your name is palindrom")
else:
    print("Not Palindrome")
