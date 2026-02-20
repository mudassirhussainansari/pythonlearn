#count even number within file

count = 0
with open("data.txt","r") as f:
    data = f.read().split(",")
    for item in data:
        if (int(item)%2 == 0):
            count +=1
print(f"Even number is {count}")
