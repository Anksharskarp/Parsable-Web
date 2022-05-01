import requests
from bs4 import BeautifulSoup
import pandas
import urllib
import sys
from pillow import Image

url = "https://en.wikipedia.org/wiki/List_of_national_parks_of_the_United_States"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
tb = soup.find('table', class_='wikitable')

url = []
filename = 1
mainURL = "https:"
for link in tb.find_all('img'):
    url = link['src']
    if (url):
        url = mainURL + url
        print(url)
        imagefile = open(str(filename) + ".jpg", 'wb')
        imagefile.write(urllib.request.urlopen(url).read())
        imagefile.close()
        filename += 1

Images = []
for p in range(1, 63):
    fname = str(p) + ".jpg"
    images.append(Image.open(fname))

newImage = Image.new('RGB', (2000, 1000))

xPos = 0
yPos = 0
for p in range(len(images)):
    newImage.paste(images[p], (xPos, yPos))
    xPos += images[i].size[0]
    if (i%9 == 8):
        xPos = 0
        yPos += images[i].size[1]

newImage.save("Park_Images.jpg")
