import math



#Assignment 1
print("Hello World!")
a = input("Enter A : ")
b = input("Enter B :")
print("Sum : ",float(a)+float(b))
print("Diff : ",float(a)-float(b))
print("Quotient : ",float(a)/float(b))
print("Remainder : ",float(a)%float(b))
print("Log : ",math.log10(float(a)))
print("Product : ",float(a)*float(b))
print("Power : ",float(a)**float(b))


#Assignment 2
miles = input("Enter miles/gallon travelled")
print(miles)
canadian_fuel_units = 235.21/float(miles);
print("fuel efficiency in Canadian units",canadian_fuel_units);

#Assignment 3
radius = input("Enter Radius")
area = math.pi * float(radius) ** 2
print(area)
volume = 4/3 * math.pi * float(radius) ** 2
print(volume)

#Assignment 4
num = input("Enter a value")
print("Floor : ",float(num)//1)
print("Ceil : ",(float(num)//1)+1)

#Assignment 5
values = input("Enter two integers seperated by commas")
val = values.split(",")
values = val[1]+","+val[0];
print(values)

#Assignment 6
name = input("Enter a name")
greeting = "You are a great person!" if(name == "John Cleese" or name == "Michael Palin") else "That is a nice name" if(name == "Neha") else "You have a nice name";
print(greeting)
