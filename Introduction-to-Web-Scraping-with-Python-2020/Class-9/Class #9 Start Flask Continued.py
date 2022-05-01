from flask import Flask, render_template
#We can create a template for faster, frictionless coding!
app = Flask(__name__)

@app.route('/') #The root -- remove the column
def index():
    return render_template('index.html', message="This website is created by William Zhang")
    #fetches the template file
    #Message is a variable. See index.html for more info

if __name__ == '__main__':
    app.run(debug=False) #Turn debug on for error-catching
