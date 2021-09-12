from tkinter import *
t=Tk()
t.title("CALCULATOR")
t.resizable(0,0)
w=400
h=480
x=(t.winfo_screenwidth()-w)/2
y=(t.winfo_screenheight()-h)/2
t.geometry("%dx%d+%d+%d"%(w,h,x,y))

a=StringVar()

def equ():
   p=a.get()
   q=eval(p)
   a.set(q)


def show(b):
    a.set(a.get()+b)

def clr():
    a.set("")

e1=Entry(font=("",25),bg="lavender",textvariable=a,justify='right')
e1.place(x=0,y=0,width=400,height=80)

b1=Button(text="7",font=("",15),bg="lightblue",fg="black",activebackground="lavender",activeforeground="black",command=lambda:show("7"))
b1.place(x=0,y=80,width=100,height=100)
b2=Button(text="8",font=("",15),bg="lightblue",fg="black",activebackground="lavender",activeforeground="black",command=lambda:show("8"))
b2.place(x=100,y=80,width=100,height=100)
b3=Button(text="9",font=("",15),bg="lightblue",fg="black",activebackground="lavender",activeforeground="black",command=lambda:show("9"))
b3.place(x=200,y=80,width=100,height=100)
b4=Button(text="+",font=("",15),bg="lightyellow",fg="black",activebackground="lavender",activeforeground="black",command=lambda:show("+"))
b4.place(x=300,y=80,width=100,height=100)

b5=Button(text="4",font=("",15),bg="lightblue",fg="black",activebackground="lavender",activeforeground="black",command=lambda:show("4"))
b5.place(x=0,y=180,width=100,height=100)
b6=Button(text="5",font=("",15),bg="lightblue",fg="black",activebackground="lavender",activeforeground="black",command=lambda:show("5"))
b6.place(x=100,y=180,width=100,height=100)
b7=Button(text="6",font=("",15),bg="lightblue",fg="black",activebackground="lavender",activeforeground="black",command=lambda:show("6"))
b7.place(x=200,y=180,width=100,height=100)
b8=Button(text="-",font=("",15),bg="lightyellow",fg="black",activebackground="lavender",activeforeground="black",command=lambda:show("-"))
b8.place(x=300,y=180,width=100,height=100)

b9=Button(text="1",font=("",15),bg="lightblue",fg="black",activebackground="lavender",activeforeground="black",command=lambda:show("1"))
b9.place(x=0,y=280,width=100,height=100)
b10=Button(text="2",font=("",15),bg="lightblue",fg="black",activebackground="lavender",activeforeground="black",command=lambda:show("2"))
b10.place(x=100,y=280,width=100,height=100)
b11=Button(text="3",font=("",15),bg="lightblue",fg="black",activebackground="lavender",activeforeground="black",command=lambda:show("3"))
b11.place(x=200,y=280,width=100,height=100)
b12=Button(text="*",font=("",15),bg="lightyellow",fg="black",activebackground="lavender",activeforeground="black",command=lambda:show("*"))
b12.place(x=300,y=280,width=100,height=100)

b13=Button(text="c",font=("",15),bg="red",fg="black",activebackground="lavender",activeforeground="black",command=clr)
b13.place(x=0,y=380,width=100,height=100)
b14=Button(text="=",font=("",15),bg="yellow",fg="black",activebackground="lavender",activeforeground="black",command=equ)
b14.place(x=200,y=380,width=100,height=100)
b15=Button(text="0",font=("",15),bg="lightblue",fg="black",activebackground="lavender",activeforeground="black",command=lambda:show("0"))
b15.place(x=100,y=380,width=100,height=100)
b16=Button(text="/",font=("",15),bg="lightyellow",fg="black",activebackground="lavender",activeforeground="black",command=lambda:show("/"))
b16.place(x=300,y=380,width=100,height=100)

t.mainloop()