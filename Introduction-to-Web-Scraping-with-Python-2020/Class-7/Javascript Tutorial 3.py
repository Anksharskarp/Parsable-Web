from selenium import webdriver
import requests

page = requests.post("http://pythonscraping.com/pages/files/processing.php", data = form)

form = {'firstname': 'Random', 'lastname': 'Person'}
print(page.text)
