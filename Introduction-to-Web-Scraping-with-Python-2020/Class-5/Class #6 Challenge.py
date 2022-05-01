#merge into one file
from urllib.request import urlopen
from bs4 import BeautifulSoup
from io import BytesIO
import PyPDF2


pdfFile = urlopen('http://https://www.cs.iupui.edu/~yuxia/WebCrawler/WarAndPeace.html')
file = open("chapter1.pdf", "wb")
file.write(pdfFile.read())

file.close()

pdfFile = open("chapter1.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(pdfFile)
pdfFileMerger = PyPDF2.PdfFileMerger()
for i in range(10):
    pdfFileMerger.append()

print(pdfReader.numPages)

for i in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(i)
    print(pageObj.extractText())

pdfFile.close()
#DON'T FORGET TO CLOSE THE FILE!!!
