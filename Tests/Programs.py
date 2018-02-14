#a.
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end='')
    print()

#b.
for i in range(0,5):
    for j in range(5-i,0,-1):
        print(j,end='')
    print()

#c.
for i in range(0,5):
    for k in range(5-1-i):
        print(' ',end = '')
    for j in range(i+1):
        print('*',end = ' ')
    print()