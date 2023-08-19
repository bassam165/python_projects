from tkinter import*
import PyPDF2

win = Tk()
win.title("calculator")
win.geometry("300x350")
def fun():
    book = open('Exception Handling.pdf','rb')
    read = PyPDF2.PdfFileReader(book)
    page = read.getPage(7)
    x = page.extractText()
    Label(win,text=" "+x).pack()

#var=StringVar()
#ent=Entry(win,textvariable=var).pack()
btn=Button(win,text="submit",command=fun).pack()
lb1=Label(win,text="your text").pack()
win.mainloop()