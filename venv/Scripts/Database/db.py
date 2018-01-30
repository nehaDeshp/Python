import pymysql
from tkinter import *

class Hotel(Frame):

    '''  Define and Connect to Db
        return database object '''

    def DB(self):
        self.root = Tk()
        self.db=None
        try:
            self.db = pymysql.connect(host="localhost", user="root", password="root", db="hotelmanagement")
            self.cursor=self.db.cursor()
        except ConnectionError as c:
            print("Connection Error")
            c.__traceback__()
        else:
            print("Success !!!")
            print("Done")
        return self.cursor

    def __init__(self):
        Frame.__init__(self)
        self.cursor = self.DB()
        self.root.title("Hotel Name")
        self.root.geometry()
        self.frame = Label(root, text="Royale Taj Vivanta", width=100, height=2)
        self.frame.grid(row=0, column=0, columnspan=6, pady=3)

        # Button(root, text="Add Rooms", command=self.addRooms).grid(row=1, column=0)
        # Button(root, text="Add Reservation", command=self.addReservation).grid(row=1, column=1)
        # Button(root, text="Find Reservation").grid(row=1, column=2)


mainloop()

