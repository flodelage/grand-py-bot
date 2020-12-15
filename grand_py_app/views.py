
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/place', methods=['POST'])
def place():
    place = request.form['place']
    return jsonify({'place':place})
