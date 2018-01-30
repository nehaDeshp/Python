from tkinter import *
import math

class calc(Frame):
    def __init__(self, master):
        master.title('Calculator')
        master.geometry()
        self.temp=0

        #Create text Area
        self.textVar = StringVar()
        self.e = Entry(master,textvariable = self.textVar)
        self.e.grid(row=0, column=0, columnspan=6, pady=3)
        self.e.focus_set()  # Sets focus on the input text area
        self.res = ""
        #Generate Button
        Button(master, text="1", width=5, command=lambda:self.inputVal(1)).grid(row=1, column=0)
        Button(master, text="2", width=5, command=lambda:self.inputVal(2)).grid(row=1, column=1)
        Button(master, text="3", width=5, command=lambda:self.inputVal(3)).grid(row=1, column=2)
        Button(master, text="4", width=5, command=lambda:self.inputVal(4)).grid(row=2, column=0)
        Button(master, text="5", width=5, command=lambda:self.inputVal(5)).grid(row=2, column=1)
        Button(master, text="6", width=5, command=lambda:self.inputVal(6)).grid(row=2, column=2)
        Button(master, text="7", width=5, command=lambda:self.inputVal(7)).grid(row=3, column=0)
        Button(master, text="8", width=5, command=lambda:self.inputVal(8)).grid(row=3, column=1)
        Button(master, text="9", width=5, command=lambda:self.inputVal(9)).grid(row=3, column=2)
        Button(master, text="0", width=5, command=lambda:self.inputVal(0)).grid(row=4, column=1)
        Button(master, text="+", width=5, command=lambda:self.inputVal('+')).grid(row=1, column=5)
        Button(master, text="-", width=5, command=lambda:self.inputVal('-')).grid(row=2, column=5)
        Button(master, text="/", width=5, command=lambda:self.inputVal('/')).grid(row=3, column=5)
        Button(master, text="*", width=5, command=lambda:self.inputVal('*')).grid(row=4, column=5)
        Button(master, text="=", width=5, command=lambda:self.btnEquals).grid(row=4, column=2)
        Button(master, text="C", width=5, command=lambda:self.btnClearDisplay).grid(row=4, column=0)

    def inputVal(self,val):
        self.res = self.res + str(val)
        self.textVar.set(self.res)


    def btnEquals(self):
        self.res = str(eval(self.res))
        self.textVar.set(self.res)

    def btnClearDisplay(self):
        text_Input.set("")

#Main
root = Tk()
obj=calc(root) #object instantiated
obj.mainloop(root)