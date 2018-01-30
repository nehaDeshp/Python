from tkinter import *

class Hotel(Frame):
    def __init__(self,root):
        Frame.__init__(self)
        root.title("Hotel Name")
        root.geometry()
        self.frame =  Label(root, text="Royale Taj Vivanta", width=100, height=2)
        self.frame.grid(row=0, column=0, columnspan=6, pady=3)

        Button(root,text="Add Rooms",command=self.addRooms).grid(row=1,column=0)
        Button(root, text="Add Reservation",command=self.addReservation).grid(row=1, column=1)
        Button(root, text="Find Reservation").grid(row=1, column=2)

    def addRooms(self):

        self.roomLabel = Label(root, text="Enter Room Number : ").grid(row=2, column=0)
        self.room_no = Entry(root).grid(row = 2,column = 1)

        self.bedTypeLable = Label(root, text="Enter Bed Type : ").grid(row=3, column=0)
        self.bedType = Entry(root).grid(row=3, column=1)

        self.smokingLabel = Label(root, text="Enter Smoking/Non Smoking : ").grid(row=4, column=0)
        self.smoking = Entry(root).grid(row=4, column=1)

        self.rateLabel = Label(root, text="Enter rate to add : ").grid(row=5, column=0)
        self.rate = Entry(root).grid(row=5, column=1)

        self.submit = Button(root,text="Save").grid(row=6,column=0)

    def addReservation(self):

        self.occupant_fnameLabel = Label(root, text="Enter First Name : ").grid(row=2, column=0)
        self.fname = Entry(root).grid(row=2, column=1)
        self.occupant_lnameLabel = Label(root, text="Enter Last Name : ").grid(row=2, column=0)
        self.lname = Entry(root).grid(row=2, column=1)


if __name__ == '__main__':
    root = Tk()
    obj = Hotel(root)
    obj.mainloop()