from tkinter import *
import tkinter.messagebox
w=Tk()
w.title('calculator')
w.geometry('500x300')
Label(w,text='Number 1').grid(row=0)
Label(w,text='Number 2').grid(row=1)
Label(w,text='Result').grid(row=2)
n1=Entry(w)
n2=Entry(w)
r=Entry(w)
n1.grid(row=0,column=1)
n2.grid(row=1,column=1)
r.grid(row=2,column=1)
def add():
    s=int(n1.get())+int(n2.get())
    r.insert(0,str(s))
def sub():
    d=int(n1.get())-int(n2.get())
    r.insert(0,str(d))
def m():
    p=int(n1.get())*int(n2.get())
    r.insert(0,str(p))
def div():
    d=int(n1.get())/int(n2.get())
    r.insert(0,str(d))
def clear():
    r.delete(0,END)
ab=Button(w,text="ADD",width=10,height=2,command=add,bg='pink',fg='brown')
ab.place(x=50,y=100)
sb=Button(w,text="SUBTRACT",width=10,height=2,command=sub,bg='light green',fg='green')
sb.place(x=170,y=100)
mb=Button(w,text="MULTIPLY",width=10,height=2,command=m,bg='brown',fg='pink')
mb.place(x=50,y=150)
db=Button(w,text="DIVIDE",width=10,height=2,command=div,bg='green',fg='light green')
db.place(x=170,y=150)
cb=Button(w,text="CLEAR",width=10,height=2,command=clear,bg='light blue',fg='blue')
cb.place(x=290,y=100)
w.mainloop()