import random

PasswordLength = input("Enter password length:")
uppercase = input("Include UpperCase? (y/n):")
lowercase = input("Include LowerCase? (y/n):")
digits = input("Include Digits? (y/n):")
symbols = input("Include Symbols? (y/n):")

passwordcode = ""
if(uppercase == "y"):
    passwordcode += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
if(lowercase == "y"):
    passwordcode += "abcdefghijklmnopqrstuvwxyz"
if(digits == "y"):
    passwordcode += "0123456789"
if(symbols == "y"):
    passwordcode += "@#$%^&*()"

if(passwordcode != ""):
    finalPassword = ""
    for _ in range(0,12):
        finalPassword += random.choice(passwordcode)
    print(finalPassword)
else:
    print("please select atleast 2 cases to generate password...!")

