cart = []

cart.append("Milk")
cart.append("Banana")
cart.append("Mango")

print(cart)

# for item in cart:
#     print(item)

flag = True

while(flag == True):
    choice = input("Do you want to remove another items yes or no: ").lower()
    if(choice == "yes"):
       cart.remove(input("Enter the item name you want to remove it: ").capitalize())
    else:
        print(cart)
        flag = False
