import random
import string

length = int(input("How long do you want your password? "))
characters = string.ascii_letters + string.digits + string.punctuation
password = ""
for i in range (length):
    password += random.choice(characters)

print(f"Your password is: {password}")
