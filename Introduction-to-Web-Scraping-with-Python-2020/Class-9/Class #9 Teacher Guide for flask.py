from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                           message="This website is created by William Zhang")


if __name__ == '__main__':
    app.run(debug=True)
