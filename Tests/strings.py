#1.
string = input("Enter a String")
strArr = string.split(" ")
string=""
for str in strArr:
    string = string + str.capitalize()+" ";
print(string)

#2.

alpha_dictionary = dict()
alpha_dictionary["ABC"] = "2"
alpha_dictionary["DEF"] = "3"
alpha_dictionary["GHI"] = "4"
alpha_dictionary["JKL"] = "5"
alpha_dictionary["MNO"] = "6"
alpha_dictionary["PQRS"] = "7"
alpha_dictionary["TUV"] = "8"
alpha_dictionary["VWXY"] = "9"
print(alpha_dictionary)
str = input("Enter String")

num = ""
for s in str:
    if(s.isalpha()):
        for item in alpha_dictionary:
            if(s.upper() in item):
                num+=alpha_dictionary[item]
    else:
        num+=s

print(num)


