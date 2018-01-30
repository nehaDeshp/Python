import pymysql
from  tkinter import *
class Hotel(Frame):

    def __init__(self,root):
        Frame.__init__(self)
        root.geometry()
        self.frame = Label(root, text="Royale Taj Vivanta", width=100, height=2)
        self.frame.grid(row=0, column=0, columnspan=6, pady=3)

        Button(root, text="Add Rooms",width=20,height=5,bg="Powder blue",command=self.addRooms).grid(row=1, column=0)
        Button(root, text="Add Reservation",width=20,height=5,bg="Powder blue",command=self.addR).grid(row=1, column=1)
        # Button(root, text="Find Reservation",width=20,height=5,bg="Powder blue",command=self.findR).grid(row=1, column=2)
        Button(root, text="Cancel Reservation", width=20, height=5, bg="Powder blue",command=self.cancel).grid(row=1, column=3)
        Button(root, text="Print Reservation", width=20, height=5, bg="Powder blue",command=self.printReservationList).grid(row=1, column=4)
        Button(root, text="Get Daily Sales", width=20, height=5, bg="Powder blue",command=lambda:self.getDailySales()).grid(row=1, column=5)
        Button(root, text="Get Occupancy Percentage", width=20, height=5, bg="Powder blue",command=lambda:self.getOccupancyPercentage()).grid(row=1, column=6)

        self.numOfRooms=12


    def addRooms(self):

        room_no = IntVar()
        bed_type = StringVar()
        smoking = StringVar()
        rate = IntVar()

        Label(root, text="Enter Room No to Add : ").grid(row=4,column=3)
        Entry(root,textvariable = room_no).grid(row=4,column=4)

        Label(root, text="Enter Bed Type to Add (King,Queen,Twin):").grid(row=5, column=3)
        Entry(root,textvariable = bed_type).grid(row=5, column=4)

        Label(root, text="Enter Smoking/Non Smoking (S/N): ").grid(row=6, column=3)
        Entry(root,textvariable = smoking).grid(row=6, column=4)

        Label(root, text="Enter Rate : ").grid(row=7, column=3)
        Entry(root,textvariable = rate).grid(row=7, column=4)

        if(room_no !=0 and bed_type !=0 and smoking !=0 and rate !=0):
            Button(root,text="Save Room Details",command=lambda:self.addRoom(room_no.get(),bed_type.get(),smoking.get(),rate.get())).grid(row= 8,column=4)

    def addRoom(self,room_no,bed_type,smoking,rate):
        database.execute("select count(occupant_name) from Room")
        count=database.fetchall()
        if(count[0][0] >= self.numOfRooms):
            print("Limit Room Exceeded !")
        else:
            database.execute("insert into `Room` (`room_no`,`bed_type`,`smoking`,`rate`,`occupant_name`,`occupied`) "
                             "values(%s,%s,%s,%s,%s,%s)",(room_no,bed_type,smoking,rate,"",'F'))
            database.execute("insert into `Hotel`(hotel_name,location,occ_cnt,hotel_id,room_id) values(%s,%s,%s,%s,%s)",
                             ('Taj', 'Mumbai', 0, 1, room_no))
            db.commit()


    def isFull(self):
        database.execute("select count(occupant_name) from Room where length(occupant_name)>0")
        count = database.fetchall()
        if(count[0][0] == self.numOfRooms):
            return True;
        return False;

    def isEmpty(self):
        database.execute("select count(occupant_name) from Room where length(occupant_name)>0")
        count = database.fetchall()
        if (count[0][0] == 0):
            return True;
        return False;

    def addR(self):

        occupant_name=StringVar()
        bed_type = StringVar()
        smoking = StringVar()

        Label(root, text="Enter Occupant Name : ").grid(row=4, column=3)
        Entry(root, textvariable=occupant_name).grid(row=4, column=4)

        Label(root, text="Enter Bed Type(King,Queen,Twin):").grid(row=5, column=3)
        Entry(root, textvariable=bed_type).grid(row=5, column=4)

        Label(root, text="Enter Smoking/Non Smoking (S/N): ").grid(row=6, column=3)
        Entry(root, textvariable=smoking).grid(row=6, column=4)

        Button(root, text="Make Reservation", command=lambda: self.addReservation(occupant_name.get(), smoking.get(), bed_type.get())).grid(
            row=8, column=4)

    def addReservation(self,occupant_name,smoking,bed_type):
        bookingDone=False
        if(self.isFull()):
            print("All Bookings are Done. Hotel is full")
        else:
            database.execute("select occupied,smoking,bed_type,room_no from Room")
            values = database.fetchall()
            for val in values:
                if(val[0] == "F"):
                    if(val[1] == smoking and val[2] == bed_type):
                        database.execute("update room set occupant_name = %s, occupied = %s where room_no = %s",(occupant_name,"T",val[3]))
                        db.commit()
                        bookingDone = True
                        break;
            if(bookingDone):
                print("Your booking is Done !")
            else:
                print("Your dont have any rooms available")

    def findR(self):
        occupant_name = StringVar()
        res = IntVar()
        Label(root, text="Enter Occupant Name to search: ").grid(row=4, column=3)
        Entry(root, textvariable=occupant_name).grid(row=4, column=4)

        Button(root, text="Find Reservation",command= lambda:res.set(self.findReservation(occupant_name.get()))).grid(row=5, column=4)
        print(res.get())
        if (res.get() == -1):
            Label(root, text="No reservation for the person ").grid(row=5, column=3)
            print()
        else:
            Label(root, text="Found. It is reserved").grid(row=5, column=3)

    def findReservation(self,name):
        NOT_FOUND = -1
        database.execute("select occupant_name from Room")
        values = database.fetchall()
        for val in values:
            if(val[0] == name):
                NOT_FOUND =  1
                break;
        return NOT_FOUND

    def cancel(self):
        occupant_name = StringVar()
        Label(root,text="Enter the name the room is to be cancelled for :").grid(row=4,column=3)
        Entry(root, textvariable=occupant_name).grid(row=5, column=3)
        Button(root, text="Cancel Reservation", command=lambda: self.cancelReservation(occupant_name.get())).grid(row=5,
                                                                                                                column=4)
    def cancelReservation(self,name):
        if(self.isEmpty() or self.findReservation(name) == -1 ):
            print("No occupant with name %s found"%name)
        else:
            database.execute("update Room set occupied = %s,occupant_name=%s where occupant_name=%s",("F","",name))
            db.commit()
            print("Reservation Cancelled for %s " % name)

    def printReservationList(self):
        if(self.isEmpty()):
            Label(root,text = "No Reservations Found").grid(row=3,column=1)
        else:
            Label(root,text="All Reserved Room Details are :").grid(row=3,column=1)
            database.execute("select * from Room where occupied = %s","T")
            data = database.fetchall()
            i=4
            for d in data:
                room_no = "Room Number : " + str(d[0])
                occ_name = "Occupant Name : "+d[2]
                sm = "Smoking Room : " + d[3]
                bed = "Bed Type: " + d[5]
                rate = "Rate : " + str(d[1])
                Label(root,text=room_no).grid(row=i,column=1)
                i += 1
                Label(root, text=occ_name).grid(row=i, column=1)
                i += 1
                Label(root, text=sm).grid(row=i, column=1)
                i += 1
                Label(root, text=bed).grid(row=i, column=1)
                i += 1
                Label(root, text=rate).grid(row=i, column=1)
                i += 1


    def getDailySales(self):
        sale=0
        database.execute("select * from Room where occupied = %s", "T")
        data = database.fetchall()
        for d in data:
            sale += d[1]
        saleVal = "Daily Sales = "+ str(sale)
        Label(root,text = saleVal).grid(row=3,column=4)
        print("Daily Sale : ",sale)

    def getOccupancyPercentage(self):
        if(not self.isEmpty()):
            database.execute("select count(occupant_name) from Room where length(occupant_name)>0")
            count = database.fetchall()
            per = "Occupancy Percentage = "+ str((count[0][0])/(self.numOfRooms)*100)
            Label(root, text=per).grid(row=3, column=4)
            print("%0.2f percent" %per)


class Room:
    def __init__(self):
        pass
    def __init__(self,room_no,bed_type,smoking,rate):
        self.__room_no = room_no
        self.__bed_type = bed_type
        self.__smoking = smoking
        self.__rate = rate

def DB():
    if __name__ == '__main__':
        global db
        db=None
        try:
            db = pymysql.connect(host="localhost", user="root", password="root", db="hotelmanagement")
            cursor=db.cursor()
        except ConnectionError as c:
            print("Connection Error")
            c.__traceback__()
        else:
            print("Success !!!")
            print("Done")
            return cursor


if __name__ == '__main__':
    database = DB()
    root = Tk()
    obj = Hotel(root)
    obj.mainloop()
    h = Hotel(root)
    db.commit()



