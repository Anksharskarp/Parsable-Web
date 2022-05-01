import requests
from bs4 import BeautifulSoup

page = requests.get("https://forecast.weather.gov/MapClick.php?lat=39.97839000000005&lon=-86.12612999999999#.Xoe-ZohKjIU")

soup = BeautifulSoup(page.content, 'html.parser')

print(soup.title)
for l in (soup.find_all('img')):
    print(l.get('src'))


items = soup.find_all('div', {'class': "tombstone-container"})

periodNames= [items.find("p", {'class': "period_name"}).get_text() for item in items]
print(periodNames)
shortDesc= [item.find("p", {'class': "short-desc"}).get_text() for item in items]
print(shortDesc)


    
