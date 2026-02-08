from tkinter import *

root = Tk()
monitor = Entry(root, width=35, borderwidth=10)
monitor.grid(row=0, column=0,columnspan=4, padx=8, pady=8)
def insert_num(number):
    now = monitor.get()
    monitor.delete(0, END) # Xóa từ chỉ mục 0 đến hết
    monitor.insert(0, str(now)+str(number))
def add():
    n1 = monitor.get()
    global num1
    global cal
    cal = "add"
    num1 = float(n1)
    monitor.delete(0, END)
def sub():
    n1 = monitor.get()
    global num1
    global cal
    cal = "sub"
    num1 = float(n1)
    monitor.delete(0, END)
def mul():
    n1 = monitor.get()
    global num1
    global cal
    cal = "mul"
    num1 = float(n1)
    monitor.delete(0, END)
def div():
    n1 = monitor.get()
    global num1
    global cal
    cal = "div"
    num1 = float(n1)
    monitor.delete(0, END)
def equal():
    if cal == "add":
        n2 = monitor.get()
        monitor.delete(0, END)
        monitor.insert(0, num1 + float(n2))
    elif cal == "sub":
        n2 = monitor.get()
        monitor.delete(0, END)
        monitor.insert(0, num1 - float(n2))
    elif cal == "mul":
        n2 = monitor.get()
        monitor.delete(0, END)
        monitor.insert(0, num1 * float(n2))
    elif cal == "div":
        n2 = monitor.get()
        monitor.delete(0, END)
        monitor.insert(0, num1 / float(n2))
    else:
        pass
def clr():
    monitor.delete(0, END)
btn1 = Button(root, text="1",padx = 20, pady=5, command=lambda : insert_num(1))
btn2 = Button(root, text="2",padx=20, pady =5, command=lambda : insert_num(2))
btn3 = Button(root, text="3",padx=20, pady=5, command=lambda : insert_num(3))
btn4 = Button(root, text="4",padx=20, pady=5, command=lambda : insert_num(4))
btn5 = Button(root, text="5",padx=20, pady=5, command=lambda : insert_num(5))
btn6 = Button(root, text="6",padx=20, pady=5, command=lambda : insert_num(6))
btn7 = Button(root, text="7",padx=20, pady=5, command=lambda : insert_num(7))
btn8 = Button(root, text="8",padx=20, pady=5, command=lambda : insert_num(8))
btn9 = Button(root, text="9",padx =20, pady=5, command=lambda : insert_num(9))
btn0 = Button(root, text="0",padx =20, pady=5, command=lambda : insert_num(0))
btnadd = Button(root,padx =19,pady=5, text="+", command=add)
btnsub = Button(root,padx =20,pady=5, text="-", command=sub)
btnmul = Button(root,padx =20,pady=5, text="*", command=mul)
btndiv = Button(root,padx =20,pady=5, text="/", command=div)
btnequal = Button(root,padx =20,pady=5, text="=", command=equal)
btndot = Button(root,padx =22,pady=5, text=".", command=lambda: insert_num("."))
btnclr = Button(root,padx =18,pady=5, text="clr", command=clr)

btn1.grid(row=3, column=0)
btn2.grid(row=3, column=1)
btn3.grid(row=3, column=2)
btn4.grid(row=2, column=0)
btn5.grid(row=2, column=1)
btn6.grid(row=2, column=2)
btn7.grid(row=1, column=0)
btn8.grid(row=1, column=1)
btn9.grid(row=1, column=2)
btn0.grid(row=4, column=0)
btnadd.grid(row=1, column=3)
btnsub.grid(row=2, column=3)
btnmul.grid(row=3, column=3)
btndot.grid(row=4, column=1)
btnequal.grid(row=4, column=2)
btndiv.grid(row=4, column=3)
btnclr.grid(row=5, column=0)

root.mainloop()

