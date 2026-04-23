# find the number in target array

number = int(input("How many item you entered: "))

nums = []

for i in range(number):
    value = int(input("Enter the element:"))
    nums.append(value)
    
target = int(input("Enter the target element you want search: "))

found = False

for i in nums:
   if i == target:
       print("your element in index: ",nums.index(i))
       break
   else:
       print("Target element not found in list")
