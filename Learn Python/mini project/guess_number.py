import random

target = random.randint(1, 100)

while True:
    userChoice = input("Enter the guess number or Quit press Q: ")
    if (userChoice == 'Q' or userChoice == 'q'):
        break
    
    if (int(userChoice) == target):
        print("You won guess succesfully")
        break
    elif (int(userChoice) > target):
        print("You choice number is greater than target please choice smaller number")
    else:
        print("You choice number is smaller than target please choice bigger number")


print("=============Game Over===========")
