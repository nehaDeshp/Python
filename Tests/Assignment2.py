'''
Create a program that reads integers from the user until a blank line is entered. Once
all of the integers have been read your program should display all of the negative
numbers, followed by all of the zeros, followed by all of the positive numbers.Within
each group the numbers should be displayed in the same order that they were entered
by the user. For example, if the user enters the values 3, -4, 1, 0, -1, 0, and -2 then
your program should output the values -4, -1, -2, 0, 0, 3, and 1. Your program
should display each value on its own line.
'''
list=[]
print("Enter Integers:")
while True:
    num = input("")
    if(num == " "):
        break
    else:
        list.append(int(num))
newlist = []
neg = []
pos = []
count=0
print(list)
for i in list:
    if(i<0):
       neg.append(i)
    elif(i>0):
        pos.append(i)
    else:
        count+=1
for i in neg:
    print(i)
for i in range(count):
    print(0)
for i in pos:
    print(i)

