from flask import Flask, render_template
import pandas


app=Flask(__name__)

@app.route('/')
def index():
    fname = 'quotes.csv'
    data = pandas.read_csv(fname)
    quoteList = list(data.values)
    return render_template('index.html', message = quoteList)


if __name__ == '__main__':
    app.run(port=9000, debug=True)
