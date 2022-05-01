from urllib.request import urlopen
from bs4 import BeautifulSoup
from io import BytesIO
import PyPDF2


pdfFile = urlopen('http://pythonscraping.com/pages/warandpeace/chapter1.pdf')
file = open("chapter1.pdf", "wb")
file.write(pdfFile.read())
# Download and write a certain file -- similar to downloading a .png or .heic
file.close()
#Don't forget to close the PDF file too!
pdfFile = open("chapter1.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(pdfFile)

print(pdfReader.numPages
#7,
# i: 0, 1, 2, 3, 4, 5, 6
#close the adobe file before opening so there isn't a permission denied error
for i in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(i)
    print(pageObj.extractText())

pdfFile.close()
#DON'T FORGET TO CLOSE THE FILE!!!
