import random
import string

password =""
password += random.choice(string.digits)
password +=  random.choice(string.punctuation)

length = int(input("Enter password length : "))

pool = string.ascii_letters
pool1 = string.digits
pool2 = string.punctuation

choice = input("Do you want numbers? (y/n): ").lower().strip()

if choice == 'y':
    print("Numbers included")
    pool = pool1 + pool
    
choice = input("Do you want symbols? (y/n): ").lower().strip()

if choice == 'y':
    print("Symbols included")
    pool = pool + pool2

remaining_length = length - len(password)

for i in range(remaining_length) :
    password += random.choice(pool) 

password = list(password)
random.shuffle(password)
password = "".join(password)

print(password)