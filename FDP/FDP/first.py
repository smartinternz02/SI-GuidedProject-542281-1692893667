from flask import Flask

app=Flask(__name__)

@app.route('/')

def welcome():
    return "Welcome to Student Assignment Submission System"

@app.route('/Greetings')

def greet():
    return "Wish you all the best"

if __name__=='__main__':
    app.run(debug=True)