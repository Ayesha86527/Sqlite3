import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

"""con=sqlite3.connect(':memory:')
con=sqlite3.connect('School.db')

cur1=con.cursor()"""
#cur1.execute("""CREATE TABLE Students (
#        Roll_No text, 
#        First_Name text,
#        Last_Name text,
#        Contact text,
#        Address text
#)""")

#cur1.execute("""
#INSERT INTO Students (Roll_no,First_Name,Last_Name,Contact,Address)
#VALUES('001','Henry','Cavill','034467463','Jersey')""")
#cur1.execute("""
#INSERT INTO Students (Roll_no,First_Name,Last_Name,Contact,Address)
#VALUES('002','Dua','Lipa','033898383','Jersey')""")

#cur1.execute("""
#INSERT INTO Students (Roll_no,First_Name,Last_Name,Contact,Address)
#VALUES('003','Henry','Holand','0456667463','Jersey')""")

#cur1.execute("""
#INSERT INTO Students (Roll_no,First_Name,Last_Name,Contact,Address)
#VALUES('004','Nancy','John','034449256','Jersey')""")

#cur1.execute("""
#INSERT INTO Students (Roll_no,First_Name,Last_Name,Contact,Address)
#VALUES('005','Ibrahim','Khan','0345673333','Jersey')""")

#con.commit()
#con.close()



m=Tk()
var1=StringVar()
var2=StringVar()
var3=StringVar()
var4=StringVar()
var5=StringVar()

def display():
    con=sqlite3.connect('School.db')
    cur1=con.cursor()
    data=cur1.execute("SELECT * FROM Students")
    for i in data:
        table.insert("",END,values=i)

def add():
    con=sqlite3.connect('School.db')
    cur1=con.cursor()
    cur1.execute("INSERT INTO Students(Roll_No,First_Name,Last_Name,Contact,Address)VALUES(?,?,?,?,?)",(var1.get(),var2.get(),var3.get(),
    var4.get(),var5.get()))
    con.commit()
    display()
    messagebox.showinfo("One record has been added!")
    con.close()

def delete():
    con=sqlite3.connect('School.db')
    cur1=con.cursor()
    cur1.execute("DELETE FROM Students WHERE Roll_No=?",(var1.get(),))
    con.commit()
    display()
    messagebox.showinfo("One record has been deleted!")
    con.close()


l1=Label(m,text="School Management System",font=('Times New Roman',40,'bold'),bg="pink",fg="blue")
l1.pack(side=TOP,fill=X)
f1=Frame(m,bg="grey")
f1.place(x=20,y=70,width=450,height=850)
l2=Label(f1,text="Roll No",bg="green",fg="white",width=15).grid(row=0,column=0,pady=10)
l3=Label(f1,text="First Name",bg="green",fg="white",width=15).grid(row=1,column=0,pady=10)
l4=Label(f1,text="Last Name",bg="green",fg="white",width=15).grid(row=2,column=0,pady=10)
l5=Label(f1,text="Contact",bg="green",fg="white",width=15).grid(row=3,column=0,pady=10)
l6=Label(f1,text="Address",bg="green",fg="white",width=15).grid(row=4,column=0,pady=10)
e1=Entry(f1,textvariable=var1,width=15)
e1.grid(row=0,column=1,padx=10,pady=10)
e2=Entry(f1,textvariable=var2,width=15)
e2.grid(row=1,column=1,padx=10,pady=10)
e3=Entry(f1,textvariable=var3,width=15)
e3.grid(row=2,column=1,padx=10,pady=10)
e4=Entry(f1,textvariable=var4,width=15)
e4.grid(row=3,column=1,padx=10,pady=10)
e5=Entry(f1,textvariable=var5,width=15)
e5.grid(row=4,column=1,padx=10,pady=10)
b1=Button(f1,width=15,bg="gold",fg="black",command=display,text="Display").grid(row=5,column=0,pady=30)
b2=Button(f1,width=15,bg="gold",fg="black",command=add,text="Add").grid(row=6,column=0,pady=30)
b3=Button(f1,width=15,bg="gold",fg="black",command=delete,text="Delete").grid(row=7,column=0,pady=30)

f2=Frame(m,bg="orange")
f2.place(x=400,y=70,width=850,height=850)
columns=('Roll No','First Name','Last Name','Contact','Address')
table=ttk.Treeview(f2,columns=columns,show="headings",height=15)
table.pack(fill=BOTH,expand=True)
for col in columns:
    table.heading(col,text=col)
    table.column(col,width=70)
m.mainloop()







