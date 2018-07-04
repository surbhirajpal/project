import tkinter
import sqlite3
from tkinter import *
import time
from PIL import Image,ImageTk


root=Tk()
root.geometry("800x400")

#table=sqlite3.connect("restaurant1.db")
#table.execute('''CREATE TABLE ORDERS
#(ORDER_NUMBER INT PRIMARY KEY NOT NULL,FRIES_MEAL INT,LUNCH_MEAL INT,BURGER_MEAL INT,PIZZA_MEAL INT,CHEESE_BURGER INT,DRINKS INT,COST INT,SERVICE_CHARGE FLOAT,TAX FLOAT,SUBTOTAL FLOAT,TOTAL FLOAT);''')
#table.commit()

def price():
    master = Tk()
    master.geometry("250x400")
    f1 = Frame(master)
    f1.pack(side=TOP)
    x = Label(f1, text="PRICE LIST", font="20")
    x.pack()

    f2 = Frame(master)
    f2.pack(side=LEFT)
    a1 = Label(f2, text="ITEMS\n\n", font="16")
    a1.pack()
    a = Label(f2, text="FRIES MEAL\n\nLUNCH MEAL\n\nBURGER MEAL\n\nPIZZA MEAL\n\nCHESSE BURGER\n\nDRINKS")
    a.pack()

    f3 = Frame(master)
    f3.pack(side=RIGHT)
    b1 = Label(f3, text="PRICE\n\n", font="16")
    b1.pack()
    b = Label(f3, text="Rs 100\n\nRs 230\n\nRs 155\n\nRs 440\n\nRs 150\n\nRs 50")
    b.pack()

    master.mainloop()

class Calculate:
    def price(self,e2,e3,e4,e5,e6,e7):
        a = e2.get()
        b = e3.get()
        c = e4.get()
        d = e5.get()
        e = e6.get()
        f = e7.get()
        costofmeal = str(int(a) * 100 + int(b) * 230 + int(c) * 155 + int(d) * 440 + int(e) * 150 + int(f) * 50)
        charge = str((int(a) * 100 + int(b) * 230 + int(c) * 155 + int(d) * 440 + int(e) * 150 + int(f) * 50) / 99)
        pay = str((int(a) * 100 + int(b) * 230 + int(c) * 155 + int(d) * 440 + int(e) * 150 + int(f) * 50) * 0.33)
        tt = str(float(costofmeal) + float(charge) + float(pay))
        cost.set(costofmeal)
        service.set(charge)
        tax.set(pay)
        final.set(tt)

def amount():
    c=Calculate()
    c.price(e2,e3,e4,e5,e6,e7)


cost=StringVar()
service=StringVar()
tax=StringVar()
final=StringVar()

def reset():
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    e7.delete(0,END)
    cost.set("")
    service.set("")
    tax.set("")
    final.set("")

#****************************************************************


frame1=Frame(root)
frame1.pack(side=TOP)
x=Label(frame1,text="RESTAURANT MANAGEMENT SYSTEM",font=("chiller","24","bold","underline"),fg="steel blue",bd=10,anchor=W)
x.grid(row=0,column=0)

localtime=time.asctime(time.localtime(time.time()))
time=Label(frame1,text=localtime,font=("century","10","bold","italic"),fg="steel blue",anchor=W)
time.grid(row=1,column=0)
#-----------------------------------------

frame2=Frame(root)
frame2.pack(side=LEFT)

lbl1=Label(frame2,text="Order No.")
lbl1.grid(row=0)
e1=Entry(frame2)
e1.grid(row=0,column=1)

lbl2=Label(frame2,text="Fries Meal")
lbl2.grid(row=1)
e2=Entry(frame2)
e2.grid(row=1,column=1)

lbl3=Label(frame2,text="Lunch Meal")
lbl3.grid(row=2)
e3=Entry(frame2)
e3.grid(row=2,column=1)

lbl4=Label(frame2,text="Burger Meal")
lbl4.grid(row=3)
e4=Entry(frame2)
e4.grid(row=3,column=1)

lbl5=Label(frame2,text="Pizza Meal")
lbl5.grid(row=4)
e5=Entry(frame2)
e5.grid(row=4,column=1)

lbl6=Label(frame2,text="Cheese Burger")
lbl6.grid(row=5)
e6=Entry(frame2)
e6.grid(row=5,column=1)

#------------------------------------

frame3=Frame(root)
frame3.pack(side=RIGHT)

lbl7=Label(frame3,text="Drinks")
lbl7.grid(row=0)
e7=Entry(frame3)
e7.grid(row=0,column=1)

lbl8=Label(frame3,text="Cost")
lbl8.grid(row=1)
e8=Entry(frame3,textvariable=cost)
e8.grid(row=1,column=1)

lbl9=Label(frame3,text="Service Charge")
lbl9.grid(row=2)
e9=Entry(frame3,textvariable=service)
e9.grid(row=2,column=1)

lbl10=Label(frame3,text="Tax")
lbl10.grid(row=3)
e10=Entry(frame3,textvariable=tax)
e10.grid(row=3,column=1)

lbl11=Label(frame3,text="Subtotal")
lbl11.grid(row=4)
e11=Entry(frame3,textvariable=cost)
e11.grid(row=4,column=1)

lbl12=Label(frame3,text="Total")
lbl12.grid(row=5)
e12=Entry(frame3,textvariable=final)
e12.grid(row=5,column=1)


#sheet.write()
# table.execute("INSERT INTO ORDERS VALUES({},{},{},{},{},{},{},{},{},{},{},{})".format(e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12))
# table.commit()

#---------------------------------

frame4=Frame(root)
frame4.pack(side=BOTTOM)
price=Button(frame4,text="price",height=3,width=10,command=price)
price.grid(row=0,column=0,padx=10,pady=10)
total=Button(frame4,text="total",height=3,width=10,command=amount)
total.grid(row=0,column=5,padx=10,pady=10)
reset=Button(frame4,text="reset",height=3,width=10,command=reset)
reset.grid(row=0,column=10,padx=10,pady=10)
exit=Button(frame4,text="exit",height=3,width=10,command=root.quit)
exit.grid(row=0,column=15,padx=10,pady=10)

#--------------------------------------------------------

mainloop()