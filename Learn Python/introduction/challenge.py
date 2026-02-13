# Count number of vowels in a string.

value = input("Enter the value you want to check the vowel: ").lower()

vowel = "aeiou"
count = 0

for i in value:
    if i in vowel:
        count +=1
print(count)