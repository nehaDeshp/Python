'''
Implement Stack and its methods
'''
list = []

def push(x):
    list.append(x)

def pop():
    if(len(list)==0):
        print("Stack is empty.. Cannot pop!")
        return
    list.delete(list[len(list)-1])

def top():
    return list[len(list)-1] if(len(list)>0) else print("No Data.")

push(10)
push(20)
push(30)

print(top())
list.pop()

print(list)