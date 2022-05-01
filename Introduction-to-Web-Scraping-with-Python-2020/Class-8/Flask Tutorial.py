#Flask is a web application framework written in Python
#pip3 install flask
#Command-C to quit the web server in the specific window that it is hosted in.
#Your First Web App
from flask import Flask #Remember to capitalize 'Flask'
import pandas

app = Flask(__name__)

@app.route('/') #If nothing is obstructing it...
def hello_world(): #The web application simply runs!
    return 'Hello, William Zhang!<style> html{background-color:lightyellow; font-size: 50px; font-type: Sans-serif}</style>' #Function returns text.

#Time to add more and more pages!
@app.route('/items')#This specifies the URL, such as 'localhost:5000/items'
def showItems(): # don't forget to redefine every new return command!
    items = pandas.read_csv('/Users/shuningliu/Documents/GitHub/Class-8/forsaleItem.csv') #Click on the file path and tap on 'copy filename as pathname'.
    return <h1> "Hi, these are the items for sale" </h1> saleitems.to_html()

if __name__ == '__main__':
    app.run()
