import tkinter
import sqlite3
from tkinter import *
import time
import random
from PIL import Image,ImageTk


root=Tk()
root.geometry("1500x500")
#table=sqlite3.connect("restaurant1.db")
#table.execute('''CREATE TABLE ORDERS
#(ORDER_NUMBER INT PRIMARY KEY NOT NULL,FRIES_MEAL INT,LUNCH_MEAL INT,BURGER_MEAL INT,PIZZA_MEAL INT,CHEESE_BURGER INT,DRINKS INT,COST INT,SERVICE_CHARGE FLOAT,TAX FLOAT,SUBTOTAL FLOAT,TOTAL FLOAT);''')
#table.commit()

def price():
    master = Tk()
    master.geometry("550x650")
    f1 = Frame(master)
    f1.pack(side=TOP)
    x = Label(f1, text="PRICE LIST\n",font=("comic sans ms","20","underline","bold"),fg="steel blue")
    x.pack()

    f2 = Frame(master)
    f2.pack(side=LEFT)
    a1 = Label(f2, text="ITEMS\n",font=("comic sans ms","15","underline"),fg="steel blue")
    a1.pack()
    a = Label(f2, text="FRIES MEAL\n\nLUNCH MEAL\n\nBURGER MEAL\n\nPIZZA MEAL\n\nCHESSE BURGER\n\nDRINKS\n\nMEAL 1-\nFRIES MEAL+BURGER MEAL+DRINKS\n\nMEAL 2-\nPIZZA MEAL+CHESSE BURGER+DRINKS",font=("comic sans ms","15"),fg="steel blue")
    a.pack()

    f3 = Frame(master)
    f3.pack(side=RIGHT)
    b1 = Label(f3, text="PRICE\n",font=("comic sans ms","15","underline"),fg="steel blue")
    b1.pack()
    b = Label(f3, text="Rs 100\n\nRs 230\n\nRs 155\n\nRs 440\n\nRs 150\n\nRs 50\n\n\nRs 250\n\n\nRs 500",font=("comic sans ms","15"),fg="steel blue")
    b.pack()

    master.mainloop()

class Calculate:
    def price(self,e2,e3,e4,e5,e6,e7,m1,m2):
        a = e2.get()
        b = e3.get()
        c = e4.get()
        d = e5.get()
        e = e6.get()
        f = e7.get()
        g = m1.get()
        h = m2.get()
        costofmeal = str(int(a) * 100 + int(b) * 230 + int(c) * 155 + int(d) * 440 + int(e) * 150 + int(f) * 50 + int(g) * 250 + int(h) *500)
        charge = str((int(a) * 100 + int(b) * 230 + int(c) * 155 + int(d) * 440 + int(e) * 150 + int(f) * 50 + int(g) * 250 + int(h) *500) / 99)
        pay = str((int(a) * 100 + int(b) * 230 + int(c) * 155 + int(d) * 440 + int(e) * 150 + int(f) * 50 + int(g) * 250 + int(h) *500) * 0.10)
        tt = str(float(costofmeal) + float(charge) + float(pay))
        cost.set(costofmeal)
        service.set(charge)
        tax.set(pay)
        final.set(tt)

def amount():
    c=Calculate()
    c.price(e2,e3,e4,e5,e6,e7,m1,m2)


ran=StringVar()
cost=StringVar()
service=StringVar()
tax=StringVar()
final=StringVar()


x=random.randint(1,500)
order=str(x)
ran.set(order)



def reset():
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    e7.delete(0,END)
    m1.delete(0, END)
    m2.delete(0, END)
    cost.set("")
    service.set("")
    tax.set("")
    final.set("")

#****************************************************************


frame1=Frame(root)
frame1.pack(side=TOP)
x=Label(frame1,text="RESTAURANT MANAGEMENT SYSTEM",font=("comic sans ms",'30',"bold","underline"),fg="steel blue",bd=10,anchor=W)
x.grid(row=0,column=0)

localtime=time.asctime(time.localtime(time.time()))
time=Label(frame1,text=localtime,font=("comic sans ms","20","bold","italic"),fg="steel blue",anchor=W)
time.grid(row=1,column=0)
#-----------------------------------------

frame2=Frame(root)
frame2.pack(side=LEFT)

lbl1=Label(frame2,text="Order No.",font=("comic sans ms","15"),fg="steel blue")
lbl1.grid(row=0)
e1=Entry(frame2,text="Order No.",textvariable=ran,font=("comic sans ms","15"),fg="steel blue")
e1.grid(row=0,column=1)

lbl2=Label(frame2,text="Fries Meal",font=("comic sans ms","15"),fg="steel blue")
lbl2.grid(row=1)
e2=Entry(frame2,font=("comic sans ms","15"),fg="steel blue")
e2.grid(row=1,column=1)

lbl3=Label(frame2,text="Lunch Meal",font=("comic sans ms","15"),fg="steel blue")
lbl3.grid(row=2)
e3=Entry(frame2,font=("comic sans ms","15"),fg="steel blue")
e3.grid(row=2,column=1)

lbl4=Label(frame2,text="Burger Meal",font=("comic sans ms","15"),fg="steel blue")
lbl4.grid(row=3)
e4=Entry(frame2,font=("comic sans ms","15"),fg="steel blue")
e4.grid(row=3,column=1)

lbl5=Label(frame2,text="Pizza Meal",font=("comic sans ms","15"),fg="steel blue")
lbl5.grid(row=4)
e5=Entry(frame2,font=("comic sans ms","15"),fg="steel blue")
e5.grid(row=4,column=1)

lbl6=Label(frame2,text="Cheese Burger",font=("comic sans ms","15"),fg="steel blue")
lbl6.grid(row=5)
e6=Entry(frame2,font=("comic sans ms","15"),fg="steel blue")
e6.grid(row=5,column=1)

meal1=Label(frame2,text="Meal 1",font=("comic sans ms","15"),fg="steel blue")
meal1.grid(row=6)
m1=Entry(frame2,font=("comic sans ms","15"),fg="steel blue")
m1.grid(row=6,column=1)
#------------------------------------

frame3=Frame(root)
frame3.pack(side=RIGHT)

meal2=Label(frame3,text="Meal 2",font=("comic sans ms","15"),fg="steel blue")
meal2.grid(row=0)
m2=Entry(frame3,font=("comic sans ms","15"),fg="steel blue")
m2.grid(row=0,column=1)

lbl7=Label(frame3,text="Drinks",font=("comic sans ms","15"),fg="steel blue")
lbl7.grid(row=1)
e7=Entry(frame3,font=("comic sans ms","15"),fg="steel blue")
e7.grid(row=1,column=1)

lbl8=Label(frame3,text="Cost",font=("comic sans ms","15"),fg="steel blue")
lbl8.grid(row=2)
e8=Entry(frame3,textvariable=cost,font=("comic sans ms","15"),fg="steel blue")
e8.grid(row=2,column=1)

lbl9=Label(frame3,text="Service Charge",font=("comic sans ms","15"),fg="steel blue")
lbl9.grid(row=3)
e9=Entry(frame3,textvariable=service,font=("comic sans ms","15"),fg="steel blue")
e9.grid(row=3,column=1)

lbl10=Label(frame3,text="Tax",font=("comic sans ms","15"),fg="steel blue")
lbl10.grid(row=4)
e10=Entry(frame3,textvariable=tax,font=("comic sans ms","15"),fg="steel blue")
e10.grid(row=4,column=1)

lbl11=Label(frame3,text="Subtotal",font=("comic sans ms","15"),fg="steel blue")
lbl11.grid(row=5)
e11=Entry(frame3,textvariable=cost,font=("comic sans ms","15"),fg="steel blue")
e11.grid(row=5,column=1)

lbl12=Label(frame3,text="Total",font=("comic sans ms","15"),fg="steel blue")
lbl12.grid(row=6)
e12=Entry(frame3,textvariable=final,font=("comic sans ms","15"),fg="steel blue")
e12.grid(row=6,column=1)


#sheet.write()
# table.execute("INSERT INTO ORDERS VALUES({},{},{},{},{},{},{},{},{},{},{},{})".format(e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12))
# table.commit()

#---------------------------------

frame4=Frame(root)
frame4.pack(side=BOTTOM)
price=Button(frame4,text="price",height=3,width=10,font=("comic sans ms","11"),fg="steel blue",command=price)
price.grid(row=0,column=0,padx=10,pady=10)
total=Button(frame4,text="total",height=3,width=10,font=("comic sans ms","11"),fg="steel blue",command=amount)
total.grid(row=0,column=5,padx=10,pady=10)
reset=Button(frame4,text="reset",height=3,width=10,font=("comic sans ms","11"),fg="steel blue",command=reset)
reset.grid(row=0,column=10,padx=10,pady=10)
exit=Button(frame4,text="exit",height=3,width=10,font=("comic sans ms","11"),fg="steel blue",command=root.quit)
exit.grid(row=0,column=15,padx=10,pady=10)

#--------------------------------------------------------

mainloop()
