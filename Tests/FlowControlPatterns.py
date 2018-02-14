#1.
print("a b pow(a,b)")
def power(a,b):
    ans=a
    for i in range(1,b):
        #print("i=",i)
        ans = ans*a
    return ans
for i in range(1,6):
    print(i,i+1,power(i,i+1))
    a=1


#3.
from random import randint
random1 = randint(1,100)
random2 = randint(1,100)
sum = input("Add %s and %s"%(random1,random2))
final = "True" if(int(sum) == int(random1)+int(random2)) else "False"
print(final)

#4.
from random import randint
import collections
lottery = randint(100,999)
print(lottery)
guess = input("Enter your lottery guess")

def matchDigit(lottery,guess):
    # l = sorted(list(str(lottery)))
    # g = sorted(list(guess))
    # print (l);
    count=0
    # compare = lambda l, g: collections.Counter(l) == collections.Counter(g)
    # if (compare(l,g) == True):
    #     return 3;
    for i in str(lottery):
        if(i in guess):
            count+=1;
    if(count == 1):
        return 1;
    if(count == 3):
        return 3;

if(guess == str(lottery)):
    reward = 10000
    print("You won $",reward)
else:
    res = matchDigit(lottery, guess)
    if(res == 3):
        reward = 3000
        print("You won $",reward)
    elif(res == 1):
        reward = 1000
        print("You won $",reward)
    else:
        print("Sorry ! Better Luck next time")


#5.
arr = []
while True:
    a = int(input("Enter Val : "))
    arr.append(a)
    if(a == 0):
        break;

if(len(arr)>1):
    pos=0
    neg=0
    total=0
    for i in range(0,len(arr)-1):
        if(arr[i] > 0):
            pos+=1;
        if(arr[i] < 0):
            neg+=1;
        total+=arr[i]
    print("The number of positives is %d" %pos)
    print("The number of negatives is %d" %neg)
    print("The total is %d" %total)
    print("The average is %0.2f" %((total)/float(len(arr)-1)))
else:
    print("0")

#6.
#a.
for i in range(1,8):
    for j in range(1,i):
        print(j,end='')
    print()
#b.
for i in range(1,7):
    for j in range(1,8-i):
        print(j,end='')
    print()
#c.
for i in range(0,6):
    for k in range(2*(6-i-1)):
        print(' ',end = '')
    for j in range(i+1,0,-1):
        print(j,end=' ')
    print()
#d.
for i in range(0,6):
    for k in range(2*i):
        print(' ',end = '')
    for j in range(1,6+1-i):
        print(j,end = ' ')
    print()

#7.
num = []
while True:
    data = int(input("Enter Integers Data :"))
    if(data == 0):
        break
    else:
        num.append(data)
max=0
count=1
for i in range(len(num)):
    if(num[i] > max):
        max=num[i]
        count=1
    elif(num[i] == max):
        count+=1
print("The largest number is ",max)
print("The occurrence count of the largest number is ",count)



