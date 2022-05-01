import requests

url = "http://www.webscrapingfordatascience.com/simplejavascript/quotes.php"
page = requests.get(url, cookies={'jsenabled': '1'})
print(page.json())
# Simple program returns javascript result
