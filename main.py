import pyttsx3
import PyPDF2

book = open('sample.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)

no_of_pages = pdfReader.numPages
print(no_of_pages)

voice = pyttsx3.init()

for i in range(0, no_of_pages):
    page = pdfReader.getPage(0)
    text = page.extractText()
    voice.say(text)
    voice.runAndWait()