from bs4 import BeautifulSoup
import requests
import pandas as pd

page = requests.get('https://en.wikipedia.org/wiki/List_of_national_parks_of_the_United_States')

soup = BeautifulSoup(page.content, 'html.parser')

parkList = soup.find('table', {"class": "wikitable sortable plainrowheaders"})

parkNames = []
states = []
rows = parkList.find_all('tr')

for i in range(1, len(rows)):
    links = rows[i].find_all('a')
    parkName = links[0].text
    state = links[2].text
    parkNames.append(parkName)
    states.append(state)

parks = pd.DataFrame(
    {'Park Name': parkNames,
     'Location': states})

parks.to_csv('parks.csv')  
