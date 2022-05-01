from urllib.request import urlopen
from bs4 import BeautifulSoup
from io import BytesIO
import PyPDF2
import requests
from zipfile import ZipFile
import docx

page = requests.get("https://www.cs.iupui.edu/~yuxia/WebCrawler/WarAndPeaceWord.html")
soup = BeautifulSoup(page.content, 'html.parser')

filename = 0
for link in soup.find_all('a'):
    url = link['href']
    wordFile = urlopen(url)
    file = open(str(filename) + ".docx", "wb")
    file.write(pdfFile.read())
    file.close()
    filename += 1
file.close()

