from flask import Flask, render_template
import pandas

app = Flask(__name__)

@app.route('/')
def homepage():
    df = pandas.read_csv('quoted.csv')
    return df.to_html()

#Unfinished. Complete in Class #11
"""
@app.route('/search', methods = ['GET', 'POST'])
def searchpage():
    df = pandas.read_csv('quoted.csv')

    if request.method == 'GET': #Receive request
        return render_template('mySearch.html')
    elif request.method == 'POST': #User searches
        return render_template('mySearch.html', )#Pass .csv file as a parameter
"""

if __name__=='__main__':
    app.run(debug = True)
