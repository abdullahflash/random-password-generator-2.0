import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
symbols = "!@#$%^&*()"

length = int(input("enter the password length:"))

inc_numbers = input("include numbers(y/n)") 
inc_symbols = input("include symbols(y/n)")

characters = letters

if inc_numbers == "y":
    characters += numbers
else :
    characters += ""

if inc_symbols == "y":
    characters += symbols
else :
    characters +=""
password = ""

for _ in range(length):
    password = password+random.choice(characters)

print("generated password",password)