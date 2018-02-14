from random import *

max = randint(1,100)
intList = []
counter=0
intList.append(max)
i=0
while (i < 99):
    val = randint(1,100)
    if(val > max):
        max = val
        counter+=1
        intList.append("%d <== Updated"%val)
    else:
        intList.append(val)
    i+=1

for i in intList:
    print(i)
print("The maximum value found was ",max)
print("The maximum value was updated %d times"%counter)