from selenium import webdriver
import requests
import pandas
from flask import Flask, render_template


driver = webdriver.Chrome(executable_path = "/Applications/chromedriver")
Quotes = []
Authors = []
Tags = []

for i in range(1, 11):
    url = "http://quotes.toscrape.com/js/page/" + str(i)
    driver.get(url)
    quotes = driver.find_elements_by_class_name('quote')
    for quote in quotes:
        quoteText = quote.find_element_by_class_name('text').text
        author = quote.find_element_by_class_name('author').text
        tags = quote.find_element_by_class_name('tags').text
        quoteText = quoteText.replace("“", "")
        quoteText = quoteText.replace("“", "")
        quoteText = quoteText.replace("“", "")
        Quotes.append(quoteText)
        Authors.append(author)
        Tags.append(tags)

Quotes = pandas.DataFrame(
    {'Quotes': Quotes,
    'Authors': Authors,
    'Tags': Tags
        })


app = Flask(__name__)

@app.route('/')
def index():
    quotes = pandas.read_csv('quotes.csv')
    return quotes.to_html()

if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

@app.route('/search')
def search():
    return render_template('index.html', quotes.to_html())
