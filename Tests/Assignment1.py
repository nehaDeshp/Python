'''
Write a program that reads integers from the user and stores them in a list. Your
program should continue reading values until the user enters 0. Then it should display
all of the values entered by the user (except for the 0) in order from smallest to largest,
with one value appearing on each line. Use either the sort method or the sorted
function to sort the list
'''

list=[]
print("Enter Integers:")
while True:
    num = int(input(""))
    if(num == 0):
        break
    else:
        list.append(num)
#sort
list.sort()
for i in list:
    print(i)
