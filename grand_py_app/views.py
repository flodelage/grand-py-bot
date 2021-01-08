
from flask import Flask, render_template, request, jsonify
from grand_py_app.utils.question_cleaner import QuestionCleaner
from grand_py_app.apis.google_maps import *


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/process', methods=['POST'])
def process():
    question = request.form['question']
    cleaner = QuestionCleaner()
    address = cleaner.address(question)
    maps = GoogleMaps()
    return jsonify({"url":maps.request_get(address)})
