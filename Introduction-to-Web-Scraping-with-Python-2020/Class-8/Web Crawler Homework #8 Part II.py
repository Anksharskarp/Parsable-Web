from flask import Flask
import pandas

app = Flask(__name__)

@app.route('/') #If nothing is obstructing it...
def show_items():
    items = pandas.read_csv('/Users/shuningliu/Documents/GitHub/Class-8/TechForSale.csv')
    return items.to_html()

if __name__ == '__main__':
    app.run()
