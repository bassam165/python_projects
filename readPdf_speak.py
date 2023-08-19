import pyttsx3 as pt
import PyPDF2 as pd
book = open('Exception Handling.pdf','rb')
read = pd.PdfFileReader(book)
spek = pt.init()
#page = read.getPage(7)
#text = page.extractText()
page=read.getNumPages()
print(page)
for i in range(0,page):
    pdf=read.getPage(i)
    text=pdf.extractText()
print(text)
spek.say(text)
spek.runAndWait()
