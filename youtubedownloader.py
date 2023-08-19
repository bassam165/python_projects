from tkinter import*
from tkinter import filedialog
from pytube import YouTube
from moviepy.editor import*

root=Tk()
root.title('video downloader')
root.geometry("400x350")

def download():
    video_path=en.get()

def getpath():
    path=filedialog.askdirectory()
    #pa.config(text=path)

la=Label(root,text="inpyt your link",bg='green',font=('Arial',20)).place(x=100,y=20)
en=Entry(root,width=10,font=('Arial 24')).place(x=100,y=80)

pa=Label(root,text="select path download",font=('Arial',12)).place(x=100,y=120)
btns=Button(root,text="select",bd=5,command=getpath).place(x=100,y=150)

down=Button(root,text="Download",bd=5,command=download).place(x=100,y=200)
root.mainloop()