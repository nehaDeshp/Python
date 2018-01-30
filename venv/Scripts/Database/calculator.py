from tkinter import *

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""

def btnSinInput():
    global operator
    X = int(operator)
    e = 2.718281828459045
    domath = (e ** (X * 1j)).imag
    text_Input.set(domath)
    operator = ""


def btnCosInput():
    global operator
    X = int(operator)
    e = 2.718281828459045
    domath = (e ** (X * 1j)).real
    text_Input.set(domath)
    operator = ""


def btnTanInput():
    global operator
    operator = int(operator)
    X = int(operator)
    e = 2.718281828459045
    domathsin = (e ** (X * 1j)).imag
    domathcos = (e ** (X * 1j)).real
    text_Input.set(domathsin / domathcos)
    operator = ""


def btnCoseInput():
    global operator
    X = int(operator)
    e = 2.718281828459045
    domath = (e ** (X * 1j)).imag
    text_Input.set(1 / domath)
    operator = ""

'''
    Instantiate a Calculator
'''
if __name__ == '__main__':

    cal = Tk()
    cal.title("Calculator")
    operator = ""
    text_Input = StringVar()
    textDisplay = Entry(cal,textvariable=text_Input, bd=30, insertwidth=4,justify='right').grid(columnspan=4)
    btn7 = Button(cal,text="7",command=lambda: btnClick(7)).grid(row=1, column=0)
    btn8 = Button(cal,text="8",command=lambda: btnClick(8)).grid(row=1, column=1)
    btn9 = Button(cal,text="9",command=lambda: btnClick(9)).grid(row=1, column=2)
    add = Button(cal,text="+",command=lambda: btnClick("+")).grid(row=1, column=3)
    btn4 = Button(cal,text="4",command=lambda: btnClick(4)).grid(row=2, column=0)
    btn5 = Button(cal,text="5",command=lambda: btnClick(5)).grid(row=2, column=1)
    btn6 = Button(cal,text="6",command=lambda: btnClick(6)).grid(row=2, column=2)
    sub = Button(cal,text="-",command=lambda: btnClick("-")).grid(row=2, column=3)
    btn1 = Button(cal,text="1",command=lambda: btnClick(1)).grid(row=3, column=0)
    btn2 = Button(cal,text="2",command=lambda: btnClick(2)).grid(row=3, column=1)
    btn3 = Button(cal,text="3",command=lambda: btnClick(3)).grid(row=3, column=2)
    mul = Button(cal,text="*",command=lambda: btnClick("*")).grid(row=3, column=3)
    btn0 = Button(cal,text="0",command=lambda: btnClick(0)).grid(row=4, column=0)
    btnClear = Button(cal,text="C",command=btnClearDisplay).grid(row=4, column=1)
    btnEqual = Button(cal,text="=",command=btnEqualsInput).grid(row=4, column=2)
    Division = Button(cal,text="/",command=lambda: btnClick("/")).grid(row=4, column=3)
    btnsin = Button(cal,text="sin",command=btnSinInput).grid(row=5, column=0)
    btncos = Button(cal,text="cos",command=btnCosInput).grid(row=5, column=1)
    btntan = Button(cal,text="tan",command=btnTanInput).grid(row=5, column=2)
    btncose = Button(cal,text="cosec",command=btnCoseInput).grid(row=5, column=3)

    cal.mainloop()