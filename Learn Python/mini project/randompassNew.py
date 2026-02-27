import random
import string

pass_length = int(input())

charValue = string.ascii_letters+string.digits+string.punctuation

randomPassword = ",".join([random.choice(charValue) for i in range(pass_length)])

print(randomPassword)
