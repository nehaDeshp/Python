from tkinter import *
def addRooms():
    print("Added")
frame = Tk()

b = Button(frame,text="Add Rooms",command=addRooms)
b.pack()


mainloop()