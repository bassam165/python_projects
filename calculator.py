from ast import operator
from dis import dis
from tkinter import *
import parser
from unittest import result

root=Tk()
root.title("calculator")

i=0
def getvariables(num):
    global i
    display.insert(i,num)
    i+=1

def get_operator(operator):
    global i
    length=len(operator)
    display.insert(i,operator)
    i+=length

def calculate():
    enter_string=display.get()
    try:
        a=parser.expr(enter_string).compile()
        result=eval(a)
        clear_all()
        display.insert(0,result)
    except:
        clear_all()
        display.insert(0,"erroe!")

def clear_all():
    display.delete(0,END)

display=Entry(root)
display.grid(row=1,columnspan=6,sticky=W+E)

Button(root,text="1",bd=8,command=lambda:getvariables(1)).grid(row=2,column=0)
Button(root,text="2",bd=8,command=lambda:getvariables(2)).grid(row=2,column=1)
Button(root,text="3",bd=8,command=lambda:getvariables(3)).grid(row=2,column=2)

Button(root,text="4",bd=8,command=lambda:getvariables(4)).grid(row=3,column=0)
Button(root,text="5",bd=8,command=lambda:getvariables(5)).grid(row=3,column=1)
Button(root,text="6",bd=8,command=lambda:getvariables(6)).grid(row=3,column=2)

Button(root,text="7",bd=8,command=lambda:getvariables(7)).grid(row=4,column=0)
Button(root,text="8",bd=8,command=lambda:getvariables(8)).grid(row=4,column=1)
Button(root,text="9",bd=8,command=lambda:getvariables(9)).grid(row=4,column=2)

Button(root,text="AC",bd=8,command=lambda:clear_all()).grid(row=5,column=0)
Button(root,text="0",bd=8,command=lambda:getvariables(0)).grid(row=5,column=1)
Button(root,text="=",bd=8,command=lambda:calculate()).grid(row=5,column=2)

Button(root,text="+",bd=8,command=lambda:get_operator("+")).grid(row=2,column=3)
Button(root,text="-",bd=8,command=lambda:get_operator("-")).grid(row=3,column=3)
Button(root,text="*",bd=8,command=lambda:get_operator("*")).grid(row=4,column=3)
Button(root,text="/",bd=8,command=lambda:get_operator("/")).grid(row=5,column=3)

root.mainloop()
