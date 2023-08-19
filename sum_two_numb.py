from tkinter import*
def add():
    x=int(e1.get())+int(e2.get())
    ent.set(x)
win=Tk()
win.title("calculator")
win.geometry("300x350")

ent=StringVar()
l1=Label(win,text="input your 1st value:",font=22)
l1.grid(row=0,column=1)
l2=Label(win,text="input your 2nd value:",font=22)
l2.grid(row=1,column=1)
l3=Label(win,text="result:",textvariable=ent,font=22)
l3.grid(row=4,column=2)

e1=Entry(win)
e2=Entry(win)
e1.grid(row=0,column=2)
e2.grid(row=1,column=2)

btn=Button(text="sum",command=add)
btn.grid(row=4,column=1)

win.mainloop()