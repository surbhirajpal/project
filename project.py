import sqlite3
from tkinter import *
import time
import random
from tkinter import messagebox
#import pillow
from PIL import Image,ImageTk

#main window GUI
root=Tk()
root.geometry("2000x650+0+0")
root.title("Restaurant Management System")
load=Image.open("food2.jpg")
background_image=ImageTk.PhotoImage(load)
background_label=Label(root,image=background_image)
background_label.place(x=0,y=0,relheight=1,relwidth=1)


#database
table=sqlite3.connect("bill.db")
table.execute('''CREATE TABLE ORDERS
(ORDER_NUMBER INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,FRIES_MEAL TEXT,LUNCH_MEAL TEXT,BURGER_MEAL TEXT,PIZZA_MEAL TEXT,CHEESE_BURGER TEXT,DRINKS TEXT,MEAL_1 TEXT,MEAL_2 TEXT,COST TEXT,SERVICE_CHARGE TEXT,TAX TEXT,SUBTOTAL TEXT,TOTAL TEXT);''')
table.commit()


#price list GUI
def price():
    master = Tk()
    master.geometry("550x650")
    master.title("Price List")
    f1 = Frame(master)
    f1.pack(side=TOP)
    x = Label(f1, text="PRICE LIST\n",font=("comic sans ms","15","underline","bold"),fg="steel blue")
    x.pack()

    f2 = Frame(master)
    f2.pack(side=LEFT)
    a1 = Label(f2, text="ITEMS\n",font=("comic sans ms","10","underline"),fg="steel blue")
    a1.pack()
    a = Label(f2, text="FRIES MEAL\n\nLUNCH MEAL\n\nBURGER MEAL\n\nPIZZA MEAL\n\nCHESSE BURGER\n\nDRINKS\n\nMEAL 1-\nFRIES MEAL+BURGER MEAL+DRINKS\n\nMEAL 2-\nPIZZA MEAL+CHESSE BURGER+DRINKS",font=("comic sans ms","15"),fg="steel blue")
    a.pack()

    f3 = Frame(master)
    f3.pack(side=RIGHT)
    b1 = Label(f3, text="PRICE\n",font=("comic sans ms","10","underline"),fg="steel blue")
    b1.pack()
    b = Label(f3, text="Rs 100\n\nRs 230\n\nRs 155\n\nRs 440\n\nRs 150\n\nRs 50\n\n\nRs 250\n\n\nRs 500",font=("comic sans ms","15"),fg="steel blue")
    b.pack()

    master.mainloop()
#-------------------------------------------------------------------------------

#assigning values to variables
ran=StringVar()
fries=StringVar()
lunch=StringVar()
burger=StringVar()
pizza=StringVar()
cheese_burger=StringVar()
drinks=StringVar()
meal_1=StringVar()
meal_2=StringVar()
cost=StringVar()
service=StringVar()
tax=StringVar()
sub_total=StringVar()
final=StringVar()

#use of class for calculations
class Calculate:
    def price(self,e2,e3,e4,e5,e6,e7,m1,m2):
        a = float(e2.get())
        b = float(e3.get())
        c = float(e4.get())
        d = float(e5.get())
        e = float(e6.get())
        f = float(e7.get())
        g = float(m1.get())
        h = float(m2.get())
        costoffries=a*100
        costoflunch=b*230
        costofburger=c*155
        costofpizza=d*440
        costofchesseburger=e*150
        costofdrinks=f*50
        costofmeal1=g*250
        costofmeal2=h*500
        costofmeal = str(int(a) * 100 + int(b) * 230 + int(c) * 155 + int(d) * 440 + int(e) * 150 + int(f) * 50 + int(g) * 250 + int(h) *500)
        charge = str((int(a) * 100 + int(b) * 230 + int(c) * 155 + int(d) * 440 + int(e) * 150 + int(f) * 50 + int(g) * 250 + int(h) *500) / 99)
        pay = str((int(a) * 100 + int(b) * 230 + int(c) * 155 + int(d) * 440 + int(e) * 150 + int(f) * 50 + int(g) * 250 + int(h) *500) * 0.10)
        subtotal=str(int(a) * 100 + int(b) * 230 + int(c) * 155 + int(d) * 440 + int(e) * 150 + int(f) * 50 + int(g) * 250 + int(h) *500)
        tt = str(float(costofmeal) + float(charge) + float(pay))
        cost.set(costofmeal)
        service.set(charge)
        tax.set(pay)
        sub_total.set(subtotal)
        final.set(tt)
        table.execute("INSERT INTO ORDERS(FRIES_MEAL,LUNCH_MEAL,BURGER_MEAL,PIZZA_MEAL,CHEESE_BURGER,DRINKS,MEAL_1,MEAL_2,COST,SERVICE_CHARGE,TAX,SUBTOTAL,TOTAL)VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",(str(costoffries),str(costoflunch),str(costofburger),str(costofpizza),str(costofchesseburger),str(costofdrinks),str(costofmeal1),str(costofmeal2),str(costofmeal),str(charge),str(pay),str(subtotal),str(tt),))
        table.commit()
        messagebox.showinfo("Success", "Bill Successfully Saved..")
        for row in table.execute("SELECT * FROM ORDERS"):
            print(row)


def amount():
    c=Calculate()
    c.price(e2,e3,e4,e5,e6,e7,m1,m2)
#------------------------------------------------------------------------


#order number
x=random.randint(1,500)
order=str(x)
ran.set(order)
#----------------------------------------------------------------


#giving default values to different variables
fries.set(0.0)
lunch.set(0.0)
burger.set(0.0)
pizza.set(0.0)
cheese_burger.set(0.0)
drinks.set(0.0)
meal_1.set(0.0)
meal_2.set(0.0)
#----------------------------------------------------------------



#function to reset all values
def reset():
    ran.set(int(order)+1)
    fries.set(0.0)
    lunch.set(0.0)
    burger.set(0.0)
    pizza.set(0.0)
    cheese_burger.set(0.0)
    drinks.set(0.0)
    meal_1.set(0.0)
    meal_2.set(0.0)
    cost.set(0.0)
    service.set(0.0)
    tax.set(0.0)
    final.set(0.0)

#------------------------------------------------------------------------

#main window GUI representation
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
e1=Entry(frame2,textvariable=ran,font=("comic sans ms","15"),fg="steel blue")
e1.grid(row=0,column=1)

lbl2=Label(frame2,text="Fries Meal",font=("comic sans ms","15"),fg="steel blue")
lbl2.grid(row=1)
e2=Entry(frame2,textvariable=fries,font=("comic sans ms","15"),fg="steel blue")
e2.grid(row=1,column=1)

lbl3=Label(frame2,text="Lunch Meal",font=("comic sans ms","15"),fg="steel blue")
lbl3.grid(row=2)
e3=Entry(frame2,textvariable=lunch,font=("comic sans ms","15"),fg="steel blue")
e3.grid(row=2,column=1)

lbl4=Label(frame2,text="Burger Meal",font=("comic sans ms","15"),fg="steel blue")
lbl4.grid(row=3)
e4=Entry(frame2,textvariable=burger,font=("comic sans ms","15"),fg="steel blue")
e4.grid(row=3,column=1)

lbl5=Label(frame2,text="Pizza Meal",font=("comic sans ms","15"),fg="steel blue")
lbl5.grid(row=4)
e5=Entry(frame2,textvariable=pizza,font=("comic sans ms","15"),fg="steel blue")
e5.grid(row=4,column=1)

lbl6=Label(frame2,text="Cheese Burger",font=("comic sans ms","15"),fg="steel blue")
lbl6.grid(row=5)
e6=Entry(frame2,textvariable=cheese_burger,font=("comic sans ms","15"),fg="steel blue")
e6.grid(row=5,column=1)

meal1=Label(frame2,text="Meal 1",font=("comic sans ms","15"),fg="steel blue")
meal1.grid(row=6)
m1=Entry(frame2,textvariable=meal_1,font=("comic sans ms","15"),fg="steel blue")
m1.grid(row=6,column=1)
#------------------------------------

frame3=Frame(root)
frame3.pack(side=RIGHT)

meal2=Label(frame3,text="Meal 2",font=("comic sans ms","15"),fg="steel blue")
meal2.grid(row=0)
m2=Entry(frame3,textvariable=meal_2,font=("comic sans ms","15"),fg="steel blue")
m2.grid(row=0,column=1)

lbl7=Label(frame3,text="Drinks",font=("comic sans ms","15"),fg="steel blue")
lbl7.grid(row=1)
e7=Entry(frame3,textvariable=drinks,font=("comic sans ms","15"),fg="steel blue")
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


#------------------------------------------------------------------

#buttons and their working
frame4=Frame(root)
frame4.pack(side=BOTTOM)
price=Button(frame4,text="price",height=3,width=10,font=("comic sans ms","11"),fg="steel blue",command=price)
price.grid(row=0,column=0,padx=10,pady=10)
total=Button(frame4,text="total",height=3,width=10,font=("comic sans ms","11"),fg="steel blue",command=amount)
total.grid(row=0,column=5,padx=10,pady=10)
reset=Button(frame4,text="reset",height=3,width=10,font=("comic sans ms","11"),fg="steel blue",command=reset)
reset.grid(row=0,column=10,padx=10,pady=10)
exit=Button(frame4,text="exit",height=3,width=10,font=("comic sans ms","11"),fg="steel blue",command=quit)
exit.grid(row=0,column=15,padx=10,pady=10)

#--------------------------------------------------------

#end of mainloop
mainloop()
