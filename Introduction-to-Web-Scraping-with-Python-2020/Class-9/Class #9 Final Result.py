from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    df = pandas.read_csv('quotes.csv')
    df.to_html()

if __name__ == '__main__':
    app.run(port=8000, debug=True)

#How to specify ports
"""
import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

app.run(port=8000, debug=True
"""
