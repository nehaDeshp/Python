'''
write a reg expression to check the whether given bank password is valid or not, assume standard bank rules for
password select and implement it, add comments if required.
'''

'''
Atleast One Caps , Atleast One Special Character , Alphanumeric, Atleast 8 characters 
At least 8 characters
Accepts 1 or more of the following
uppercase letters: A-Z
lowercase letters: a-z
numbers: 0-9
any of the special characters: @#$%^&+=
'''

import re
regEx = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"
password = input("Enter Password :")
isValid = re.match(regEx,password)

if(isValid):
    print("Password is Valid")
else:
    print("Passwrd not valid")