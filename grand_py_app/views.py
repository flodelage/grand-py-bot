
from flask import Flask, render_template, request, jsonify
from .utils.question_cleaner import QuestionCleaner

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/process', methods=['POST'])
def process():
    question = request.form['question']
    cleaner = QuestionCleaner(question)
    return jsonify({'question': cleaner.remove_punctuations})
