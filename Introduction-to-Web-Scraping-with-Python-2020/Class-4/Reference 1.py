import requests
from bs4 import BeautifulSoup
import pandas
import urllib

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
