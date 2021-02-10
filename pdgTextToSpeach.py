import pyttsx3
import PyPDF2

book = open('oop.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
friend = pyttsx3.init()
page = pdfReader.getPage(20)
text = page.extractText()
friend.say(text)
friend.runAndWait()
