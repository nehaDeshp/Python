from tkinter import *
import sqlite3

class Sorting(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.function = {1:self.quick, 2:self.bubble,3:self.selection}
        self.master.title("Quick Sort Algorithm")
        self.master.rowconfigure(5, weight=1)
        self.master.columnconfigure(5, weight=1)
        self.grid(sticky=W+E+N+S )

        #label for sort intro
        self.label1 = Label(self, text="Quick Sort Algorithm by reading elements from database", width=50, height=2)
        self.label1.grid(row=0, column=1, columnspan = 4, sticky=N)

        #Radio buttons with sorting name
        self.v = IntVar() #integer variable
        indx=1 # this determines location and the value returned by this button
        button1 = Radiobutton(self, text='Quick Sort', variable=self.v, value=indx)
        button1.grid(row=1, column=indx, sticky=W+E+N+S)

        indx = 2
        button4 = Radiobutton(self, text='Bubble Sort', variable=self.v, value=indx)
        button4.grid(row=1, column=indx, sticky=W + E + N + S)

        indx = 3
        button5 = Radiobutton(self, text='Selection Sort', variable=self.v, value=indx)
        button5.grid(row=1, column=indx, sticky=W + E + N + S)


        self.button4 = Button(self,text='select the sorting, click here to read values from the Table',command=self.gen, bg = "cyan")
        self.button4.grid(row=2, column=1, columnspan=3, sticky=W+E+N+S)
        self.rowconfigure(5, weight=1)
        self.columnconfigure(5, weight=1)

        print(self.function)

    def create_but2sort(self):
        self.button5 = Button(self, text='click here to sort the above values using the selected sort', command=self.sortit, bg = "deep sky blue")
        self.button5.grid(row=4, column=1, columnspan=3, sticky=W+E+N+S)
        self.rowconfigure(5, weight=1 )
        self.columnconfigure(5, weight=1)

    def gen(self):
        # write a database code to get from database and display here
        conn = sqlite3.connect("data.db")
        conn.row_factory = lambda cursor, row: row[0]
        c = conn.cursor()
        self.nums = c.execute('SELECT * FROM values_sorting').fetchall()
        print("Elements before sorting")
        print(self.nums)
        num = ''.join('%4i' % num for num in self.nums)
        self.label2 = Label(self, text=num, width=2, height=2)
        self.label2.grid(row =3, columnspan=10, sticky = W+E+N+S)
        self.create_but2sort()

    def sortit(self):
        function = self.function[self.v.get()]
        result = function()
        print("Elements after sorting")
        print(result)
        num = ''.join('%4i' % num for num in result)
        self.label3 = Label(self, text=num, width=2, height=2)
        self.label3.grid(row=5, columnspan=10, sticky=W+E+N+S )

    def quick(self):
        print('implementing quick sort algorithm ')
        return sorted(self.nums)

    def slow(self):
        print('implementing slow sort algorithm ')
        time.sleep(5)
        return sorted(self.nums)

    def medium(self):
        print('implementing medium sort algorithm ')
        time.sleep(2)
        return sorted(self.nums)

    def bubble(self):
        print('implementing Bubble sort algorithm ')
        for i in range(len(self.nums)):
            for j in range(len(self.nums)):
                if(self.nums[i]<self.nums[j]):
                    temp=self.nums[i]
                    self.nums[i] = self.nums[j]
                    self.nums[j]=temp
        return self.nums

    def selection(self):
        print('implementing Selection sort algorithm ')
        self.nums = self.nums[:]
        out = []
        while self.nums:
            smallest = min(self.nums)
            self.nums.remove(smallest)
            out.append(smallest)

        return out

def main():
    Sorting().mainloop()

if __name__ == "__main__":
    main()