# 10 to 1 reverse multiplication table

value = int(input("Enter the value: "))

for i in range(10, 0, -1):
    print(f"{value} X {i} = {value*i}")
