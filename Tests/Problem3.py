''' Enter Number of requests'''
n = int(input())

starting_day = []
ending_day = []

'''Enter Start and End Date'''
start = input()
end = input()

''' Store in List'''
for i in range(n):
    starting_day = start.split(" ")
    ending_day = end.split(" ")

'''create tuples'''

out=[]
req = zip(starting_day,ending_day)
for i in range(n):
    request = req.__next__()
    if(int(request[0]) < int(request[1])):
        print(request)
        out.append(tuple(request))

print(out)
sorted(out,key=out[0])
'''print tuples
print(len(out))
for o in out:
    print(o,end=" ")
'''
