from urllib.request import urlopen
from bs4 import BeautifulSoup
from io import BytesIO
import PyPDF2
import requests

page = requests.get('https://www.cs.iupui.edu/~yuxia/WebCrawler/WarAndPeace.html')
soup = BeautifulSoup(page.content, 'html.parser')

filename = 0
for link in soup.find_all('a'):
    url = link['href']
    pdfFile = urlopen(url)
    file = open(str(filename) + ".pdf", "wb")
    file.write(pdfFile.read())
    file.close()
    filename += 1

pdfMerger = PyPDF2.PdfFileMerger()
for i in range(filename):
    pdfMerger.append(PyPDF2.PdfFileReader(str(i) + ".pdf"), 'rb')
    #'rb' is reading binary format
with open("Merged.pdf", 'wb') as f:
    pdfMerger.write(f)
#Another way to open a file
"""
file = open("Merged.pdf", "wb")
pdfMerger.write(file)
file.close()
"""
