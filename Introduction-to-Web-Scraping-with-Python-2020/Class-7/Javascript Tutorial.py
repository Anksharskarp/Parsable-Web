#driver = webdriver.Chrome(executable_path = "~/Library/users/shuningliu/Documents/chromedriver")
#chrome_driver, firefox_driver, safari_driver, ie_driver ('<path to webdriver>')
from selenium import webdriver
url = "http://www.webscrapingfordatascience.com/complexjavascript/"
driver = webdriver.Chrome("~/Documents/GitHub/Class-7/chromedriver")
driver.implicitly_wait(10)
driver.get(url) #Similar to requests Library
quotes = driver.find_element_by_class_name('quote')
for quote in quotes:
    print(quote.text)

#Tags identifier
#find_element_by_id: Use id to find an element.
#find_element_by_name: Use name to find an element.
#find_element_by_link_text: Use text value of a link to find element.
#find_element_by_partial_link_text: Find element by matching part of a hyper link text(anchor tag).
#find_element_by_tag_name: Use tag name to find an element.
#find_element_by_class_name: Use value of class attribute to find an element.
#find_element_by_css_selector: Use CSS selector for id, class to find element. 
