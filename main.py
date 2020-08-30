import pyttsx3
import PyPDF2
book=open('milon.pdf','rb')

pdfReader=PyPDF2.PdfFileReader(book)

pages=pdfReader.numPages
print(pages)

student=pyttsx3.init()
for num in range(7,pages):
    page=pdfReader.getPage(num)
    text=page.extractText()
    student.say(text)
    student.runAndWait()
