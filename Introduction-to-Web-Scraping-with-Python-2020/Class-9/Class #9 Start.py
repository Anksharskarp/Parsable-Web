from selenium import webdriver
import pandas

driver = webdriver.Chrome(executable_path = "/Applications/chromedriver")
quoteList = []

for i in range(1, 11):
    url = "http://quotes.toscrape.com/js/page/" + str(i)
    driver.get(url)
    #Selenium webdriver obtains url
    quotes = driver.find_elements_by_class_name('quote')
    #Searches all elements with the class 'quotes'
    for quote in quotes:
        quoteText = quote.find_element_by_class_name('text').text
        author = quote.find_element_by_class_name('author').text
        #Removes the annoying quotation marks:
        quoteText = quoteText.replace("“", "")
        quoteText = quoteText.replace("“", "")
        #Stay in singular format for element to avoid attribute errors...
        #print(quoteText, author)

        oneQuote = ((quoteText, author))
        quoteList.append(oneQuote)
print(quoteList)

df = pandas.DataFrame(quoteList, columns=['quote', author])
df.to_csv('quotes.csv')
