'''
implement queue FIFO principle using list and its methods
'''

queue = []
front=0
rear=-1

def insertQ(x):
    queue.append(x)
    global rear
    rear+=1

def removeQ():
    global front
    if(front==rear):
        print("List is empty. Cannot delete")
        return
    queue.remove(queue[front])
    front=front+1

insertQ(10)
insertQ(20)
insertQ(30)
insertQ(40)
print(queue)

removeQ()
print(queue)
print(front)