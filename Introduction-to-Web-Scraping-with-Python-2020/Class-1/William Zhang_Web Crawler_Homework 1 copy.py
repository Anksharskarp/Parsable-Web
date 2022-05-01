from bs4 import BeautifulSoup
import requests
page = requests.get("https://www.pbs.org/shows/")

soup = BeautifulSoup(page.content, 'html.parser')

popShows = soup.find_all('li', {"class": "shows-dropdown__popular-show"})
for p in popShows:
    print(p.text)
    







