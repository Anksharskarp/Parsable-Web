from bs4 import BeautifulSoup
import requests
import urllib
from PIL import Image

url = ('http://www.pythonscraping.com/pages/warandpeace.html')

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

charList = page.text

charLen = len(str(charList))
print(charLen)
