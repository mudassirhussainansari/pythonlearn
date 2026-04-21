""" Age category:
<13 → Child
13–19 → Teen
20–59 → Adult
60+ → Senior """

try:
    age = float(input("Enter the age: "))
    
    if age < 0:
        print("please enter age is greater than or equal 0")
    elif age < 13:
        print("child")
    elif age <= 19:
        print("Teen")
    elif age <= 59:
        print("Adult")
    else:
        print("Senior")
except ValueError:
    print("Invalid value please enter right value like number",ValueError)
