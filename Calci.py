from tkinter import *

expression=""

root=Tk()
root.title("Calculator")
root.configure(bg="grey")

lbl=Label(root,text="Simple Calculator",font=(30),bg="Green").grid(row=0,column=0,columnspan=4)
eqn=StringVar()
screen=Entry(root,font=(30),width=20,textvariable=eqn)
screen.grid(row=1,column=0,columnspan=4,pady=15)

#Functions
def values(key):
    global expression
    cur=screen.get()
    expression=expression+str(key)
    eqn.set(expression)
    
def clear():
    global expression
    expression=""
    eqn.set(expression)

def equal():
    global expression
    try:
        result=eval(expression)
        eqn.set(result)
    except ZeroDivisionError:
        eqn.set("Can't divide by zero")
    except Exception:
        eqn.set("Syntax Error")
    expression=""

#Keys
but_7=Button(root,text=7,command=lambda :values(7),width=10,bg="cyan").grid(row=3,column=0)
but_8=Button(root,text=8,command=lambda :values(8),width=10,bg="cyan").grid(row=3,column=1)
but_9=Button(root,text=9,command=lambda :values(9),width=10,bg="cyan").grid(row=3,column=2)

but_4=Button(root,text=4,command=lambda :values(4),width=10,bg="cyan").grid(row=4,column=0)
but_5=Button(root,text=5,command=lambda :values(5),width=10,bg="cyan").grid(row=4,column=1)
but_6=Button(root,text=6,command=lambda :values(6),width=10,bg="cyan").grid(row=4,column=2)

but_1=Button(root,text=1,command=lambda :values(1),width=10,bg="cyan").grid(row=5,column=0)
but_2=Button(root,text=2,command=lambda :values(2),width=10,bg="cyan").grid(row=5,column=1)
but_3=Button(root,text=3,command=lambda :values(3),width=10,bg="cyan").grid(row=5,column=2)

but_0=Button(root,text=0,command=lambda :values(0),width=10,bg="cyan").grid(row=6,column=0)
but_00=Button(root,text="00",command=lambda :values("00"),width=10,bg="cyan").grid(row=6,column=2)
but_dot=Button(root,text=".",command=lambda :values("."),width=10,bg="cyan").grid(row=6,column=1)


but_add=Button(root,text="+",command=lambda :values("+"),width=10,bg="cyan").grid(row=6,column=4)
but_sub=Button(root,text="-",command=lambda :values("-"),width=10,bg="cyan").grid(row=5,column=4)
but_pro=Button(root,text="x",command=lambda :values("*"),width=10,bg="cyan").grid(row=4,column=4)
but_div=Button(root,text="/",command=lambda :values("/"),width=10,bg="cyan").grid(row=3,column=4)

but_clr=Button(root,text="CLR",command=clear,width=22,bg="cyan").grid(row=7,column=0,columnspan=2)
btn_eql=Button(root,text="=",width=10,command=equal,bg="cyan").grid(row=7,column=2,columnspan=2)


root.mainloop()
