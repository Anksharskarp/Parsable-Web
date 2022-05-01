import requests
from bs4 import BeautifulSoup

page= requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
page

soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())

list(soup.children)
[type(item) for item in list(soup.children)]

html = list(soup.children)[2]
list(html.children)

body = list(html.children)[3]
list(body.children)

p = list(body.children)[1]
p.get_text()

