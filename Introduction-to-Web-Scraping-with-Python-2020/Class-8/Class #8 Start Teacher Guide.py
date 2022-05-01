import requests
from bs4 import BeautifulSoup
import pandas

url = "https://indianapolis.craigslist.org/search/sss?query=for+sale&sort=rel&search_distance=10&postal=46033&max_price=500"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

items = soup.find_all('li', class_= "result-row")

titles = []
prices = []
for item in items:
    title = item.find('a', class_="result-title hdrlnk")
    price = item.find('span', class_="result-price")
    titles.append(title.get_text())
    prices.append(price.get_text())

forsaleItems = pandas.DataFrame(
    {'Title': titles,
    'Price': prices
        })

forsaleItems.to_csv('forsaleItem.csv', index = False) #Removes index numbering from .csv file

#Next, we attempt to remove the index numbering for the chart
#on the X and Y axis.
