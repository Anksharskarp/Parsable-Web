from bs4 import BeautifulSoup
import requests
from matplotlib import *

url = "https://www.imdb.com/title/tt0285335/"
episodes = []
ratings = []

for season in range (1, 31):
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
