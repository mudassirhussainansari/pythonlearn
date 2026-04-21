# ATM withdrawal:

# Balance < amount → "Insufficient funds"
# Else → "Success"

amount = float(input("Enter the amount: "))

balance = 1000

if balance < amount:
    print("Insufficient funds")
else:
    balance = balance - amount
    print("Success")
    print("Your current balance: ", balance)
