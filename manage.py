from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to my Flask app!'

@app.route('/greetings/')
def greetings():
    return 'Please enter a valid greeting URL'

@app.route('/greetings/winter')
def winter_greeting():
    return 'Happy Holidays!'

@app.route('/greetings/newyear')
def new_year_greeting():
    return 'Happy New Year!'

if __name__ == '__main__':
    app.run(debug=True)
