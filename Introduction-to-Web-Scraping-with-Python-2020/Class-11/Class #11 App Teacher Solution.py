from flask import Flask, render_template, request
import pandas

app=Flask(__name__)

@app.route('/')
def homepage():
    df = pandas.read_csv('quoted.csv')
    return df.to_html()


@app.route('/search', methods=['GET', 'POST'])
def searchpage():
    data = pandas.read_csv('quoted.csv', header=0)
    quoteList = list(data.values)

    if request.method == 'GET':
        return render_template('mySearch.html', quoteList=quoteList, author=None)
    elif request.method == 'POST':
        author = request.form['author']
        return render_template('mySearch.html', quoteList=quoteList, author=author)

if __name__=='__main__':
    app.run(debug= True)
