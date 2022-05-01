from selenium import webdriver
url = "https://www.cs.iupui.edu/~yuxia/WebCrawler/JavascriptExample.html"
driver = webdriver.Chrome("~/Documents/GitHub/Class-7/chromedriver")

driver.implicitly_wait(10)

driver.get(url) #Similar to requests Library

myText = driver.find_element_by_class_name('txt')
print(myText.text)
