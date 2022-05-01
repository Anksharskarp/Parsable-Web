from bs4 import BeautifulSoup
import requests
import pandas as pd
import urllib

page = requests.get('https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States')

soup = BeautifulSoup(page.content, 'html.parser')

tb = soup.find('table', {"class": "wikitable"})
#Look for:
#    "<img src=""></img>"

filename = 1
for link in tb.find_all('img'):
    url = link['src']
    print(url)
    imageFile = open(str(filename)+".jpeg", 'wb')
    url = "https:" + url 
    imageFile.write(urllib.request.urlopen(url).read())
    imageFile.close()
    #close the file to save changes and prevent accidental overwriting
    filename +=1                                   
    
