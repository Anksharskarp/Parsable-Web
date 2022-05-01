from bs4 import BeautifulSoup
import requests
import urllib
from PIL import Image

url = ('http://www.pythonscraping.com/pages/warandpeace.html')
soup = BeautifulSoup(page.content, 'html.parser')

nameList = soup.find_all('span', {'class': 'green'})
print(len(nameList))

timesPrince = soup.find_all(text = 'the prince')
print(timesPrince)
print(len(timesPrince))
