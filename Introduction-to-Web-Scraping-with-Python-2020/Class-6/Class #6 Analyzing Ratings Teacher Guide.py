import requests
from bs4 import BeautifulSoup
from matplotlib.pyplot import *

url = 'http://www.imdb.com/title/tt0458290/episodes'
episodes = []
ratings = []
for season in range(6, 8):
    r = requests.get(url, params={'season': season})
    soup = BeautifulSoup(r.text, 'html.parser')
    listing = soup.find('div', class_='eplist')
    for epnr, div in enumerate(listing.find_all('div', class_='ipl-rating-star small'), 1):
        episode = "{}.{}".format(season, epnr)
        rating_el = div.find(class_='ipl-rating-star__rating')
        rating = float(rating_el.get_text(strip=True))
        print('Episode:', episode, '-- rating:', rating)
        episodes.append(episode)
        ratings.append(rating)

figure()
positions = [a*2 for a in range(len(ratings))]
bar(positions, ratings, align='center')
show()
