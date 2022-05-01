import pandas as pd
from selenium import webdriver

driver = webdriver.Chrome(executable_path = "/Applications/chromedriver")
total = []

for page in range(1,11):

    url = "http://quotes.toscrape.com/js/page/" + str(page) + "/"
    driver.get(url)
    quotes = driver.find_elements_by_class_name("quote")

    for quote in quotes:
        quote_text = quote.find_element_by_class_name('text').text
        quote_text = quote_text.replace('“', '')
        author = quote.find_element_by_class_name('author').text
        tags = quote.find_element_by_class_name('tags').text
        tags = tags[6:]
        if (not tags):
            print("tags empty")
            tags="None"
        new = ((quote_text,author, tags))
        total.append(new)

df = pd.DataFrame(total,columns=['quote','author', 'tags'])
#df.to_csv('quoted.csv', index=False)
df.to_csv('quoted.csv')
driver.close()
