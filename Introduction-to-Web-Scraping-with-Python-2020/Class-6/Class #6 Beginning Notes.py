from bs4 import BeautifulSoup
import requests

url = "https://www.imdb.com/title/tt0458290/episodes?"

for season in range(1, 8):
    r = requests.get(url, params = {'season': season})
    soup = BeautifulSoup(r.text, 'html.parser')
    eList = soup.find('div', class_='eplist')
    # or...
   #elist = soup.find('div', 'class' : 'eplist')
    eNumber = 1
    for episode in eList.find_all('div', class_='ipl-rating-star small'):
        eFullNumber = '{} . {}'.format(season, eNumber) #Formatter in str.
        rating = episode.find(class_='ipl-rating-star__rating')
        print('Episode: ', eFullNumber, '-- Rating: ', rating.get_text())#You can omit the () at the end of the tag 'text'
        eNumber += 1
