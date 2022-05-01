from csv import reader
from bs4 import BeautifulSoup
import requests

opened_file = open('MontyPythonAlbums.csv')
read_file = reader(opened_file)
MontyPythonAlbums = list(read_file)

years = []
for row in MontyPythonAlbums[1:]:
    year = int(row[1])
    years.append(year)
median_value = float((years[8] + years[9])/2)
print(median_value)
