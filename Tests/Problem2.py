'''
Issues :
1.Handle space issue
    Solution 1(Efficient):
    After input we can check for pattern[A-Z][0-9][A-Z\s][A-Z][0-9][A-Z]
    Pattern matching not implemented
    Solution 2:
    While giving input we can check each character if it is digit , number or space,
    if valid pattern we can trim the space
2.List display or
    for province , (X = we are getting 2 values)
    Solution we can use a loop
'''

dictionary = {
    "A" : "Newfoundland",
    "B" : "Nova Scotia",
    "C" : "Prince Edward Island",
    "E" : "New Brunswick",
    "G" : "Quebec",
    "H" : "Quebec",
    "I" : "Quebec",
    "K" : "Ontario",
    "L" : "Ontario",
    "M" : "Ontario",
    "N" : "Ontario",
    "P" : "Ontario",
    "R" : "Manitoba",
    "S" : "Saskatchewan",
    "T" : "Alberta",
    "V" : "British Columbia",
    "X" : ["Nunavut","NorthwestTerritories"],
    "Y" : "Yukon"
}
address_type = {
    "0" : "Rural",
    "1" : "Urban"
}

postal_code = input("Enter a Canadian Postal Code")
valid=False
invalid_province = ["D","F","I","O","Q","U","W","Z"]
invalid_type    = ["0","1"]

if(len(postal_code) == 6):
    if(postal_code[1].isdigit() and postal_code[3].isdigit() and postal_code[5].isdigit()
        and postal_code[0].isalpha() and postal_code[2].isalpha() and postal_code[4].isalpha()):
        if postal_code[0] not in invalid_province and postal_code[1] in invalid_type:
            valid=True
            province = dictionary.get(postal_code[0])
            type = address_type.get(postal_code[1])
            print("The postal code is for %s address in %s" %(type,province))
if(valid == False):
    print("Invalid Postal Code")
