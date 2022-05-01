from zipfile import ZipFile
from urllib.request import urlopen
from bs4 import BeautifulSoup
from io import BytesIO
#All statements are case sensitive and extremely important. Failure to do so can result in syntax error
#Always use pip3 install if there are any potential difficulties
wordFile = urlopen('http://pythonscraping.com/pages/AWordDocument.docx').read()
byteFile = BytesIO(wordFile)
document = ZipFile(byteFile)
xmlContent = document.read('word/document.xml')
wordObj = BeautifulSoup(xmlContent.decode('utf-8'), 'xml')
#Try lxml if xml returns numerous annoying tags around the text.
#We are now using the xml parser instead of the html parser. Note the important difference
textObj = wordObj.find_all('w:t')
for txtElem in textObj:
    print(txtElem.text)
