import requests
from bs4 import BeautifulSoup
import pandas

titles=[]
prices=[]
for i in range(1, 51):
    url = "http://books.toscrape.com/catalogue/page-{}.html".format(i)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    books = soup.find_all('article', {'class':'product_pod'})
    for book in books:
        title = book.find('h3').find('a')['title']
        titles.append(title)
        price = book.find('p', class_='price_color').text
        priceClean = ''.join(i for i in price if i.isdigit() or i=='.')
        prices.append(priceClean)

bookData = pandas.DataFrame(
    {'Title': titles,
     'Prices': prices,
        }
    )
bookData.to_csv('book.csv')
