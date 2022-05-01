from bs4 import BeautifulSoup
import requests
import urllib

url = "https://indianapolis.craigslist.org/search/sss?query=for+sale&sort=rel&search_distance=10&postal=46033&max_price=500"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

Stuff = []
Prices = []
itemName = soup.find_all('a', class_="result-title hdrlnk")
for item in itemName:
    Stuff.append(item.get_text())

itemPrice = soup.find_all('span', class_="result-price")
for price in itemPrice:
    Prices.append(price.get_text())
print(Stuff)
print(Prices)
