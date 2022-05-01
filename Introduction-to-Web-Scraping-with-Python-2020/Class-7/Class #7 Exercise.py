from bs4 import BeautifulSoup
import requests
import pandas as pd

for i in range (1, 3):
    url = "http://books.toscrape.com/catalogue/page-{}.html".format(i)#Notice the brackets after page- Fill brackets with int 1 to 51
    #Careful!!!! Avoid the www. May cause errors.
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    books = soup.find_all("article", class_="product_pod")
    #print(books.get_text())
    Book_Price = []
    Book_Name = []
    for book in books:
        bookLink = book.find('h3').find('a')['title']#Find, in <h3>, the link with class title.
        price = book.find('p', class_='price_color')
        priceClean = ''.join(i for i in price if i.isdigit() or i=='.')#Removes messy symbols
        Book_Price.append(price)
        Book_Name.append(bookLink)


name_dict = {
            'Book Name': Book_Name,
            'Price': Book_Price
          }

df = pd.DataFrame(name_dict)

print(df)
df.to_csv('booksData.csv')
