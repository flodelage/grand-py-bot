
from flask import Flask, render_template, request, json


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/place', methods=['POST'])
def signUpUser():
    place =  request.form['place'];
    return json.dumps({'status':'OK','place':place});


if __name__=="__main__":
    app.run()
