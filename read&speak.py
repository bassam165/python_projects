from importlib.resources import contents
from tkinter import*
from tkinter import ttk
from tkinter import filedialog as fd
import PyPDF2
import pyttsx3
win=Tk()
win.title("File Reading")
win.geometry("765x450")
#file=fd.askopenfile()
text = Text(win)
text.grid(column=0, row=0)
def open_file():
    f=fd.askopenfilename()
    pdf=PyPDF2.PdfFileReader(f)
    page=pdf.getNumPages()
    for i in range(0,page):
        read=pdf.getPage(i)
        content=read.extractText()
        text.insert('1.0',content)
#def spk():
    #spek=pyttsx3.init()
    #spek.say(contents)
    #spek.runAndWait()
    
btn=Button(win,text="open file",command=open_file)
btn.grid()
#btn=Button(win,text="speak",command=spk)
#btn.grid()
win.mainloop()