from bs4 import BeautifulSoup
import requests
import pandas
from flask import Flask

url = "https://indianapolis.craigslist.org/search/sss?query=computer&sort=rel"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

products = []
cost = []

computerProducts = soup.find_all('p', class_="result-info")


for computer in computerProducts:
    stuff = computer.find('a', class_="result-title hdrlnk")
    price = computer.find('span', class_="result-price")
    products.append(stuff.get_text())
    cost.append(price.get_text())
print(products)
print(cost)
TechForSale = pandas.DataFrame(
    {'Title': products,
    'Price': cost
        })

TechForSale.to_csv('TechForSale.csv', index = False)

app = Flask(__name__)

@app.route('/') #If nothing is obstructing it...
def show_items():
    items = pandas.read_csv('/Users/shuningliu/Documents/GitHub/Class-8/TechForSale.csv')
    return items.to_html()

if __name__ == '__main__':
    app.run()
