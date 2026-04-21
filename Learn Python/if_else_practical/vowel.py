# Check if a character is vowel or consonant

char = input("Enter the char: ")

if len(char) != 1:
    print("Enter only one character")
elif not char.isalpha():
    print("it is not alphabet character")
elif char.lower() in "aeiou":
    print(char,"is vowel")
else:
    print(char,"is consonant")
