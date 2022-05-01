from bs4 import BeautifulSoup
import requests
import pandas as pd

titles = []

for i in range(1, 51):
    url = "http://books.toscrape.com/catalogue/page-{}.html".format(i)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    books = soup.find('article', {'class': 'product_pod'})
    for book in books:
        if book.find('div', {'class': 'image_container'}).get_text() == 'star-rating Four' or book.find('div', {'class': 'image_container'}).get_text() == 'star-rating Five':
            title = book.find('h3').find('a')['title']
            titles.append(title)
            price = book.find('p', class_='price_color').text
            priceClean = ''.join(i for i in price if i.isdigit() or i=='.')
            prices.append(priceClean)
print(titles)
