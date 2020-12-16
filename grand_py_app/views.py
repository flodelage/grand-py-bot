
from flask import Flask, render_template, request, jsonify
from grand_py_app.utils.question_cleaner import QuestionCleaner


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/process', methods=['POST'])
def process():
    question = request.form['question']
    cleaner = QuestionCleaner()
    return jsonify({'question': cleaner.remove_all(question)})
