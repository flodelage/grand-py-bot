
from flask import Flask, render_template, request, jsonify
from grand_py_app.utils.response import Response


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/process', methods=['POST'])
def process():
    question = request.form['question']
    response = Response()
    return jsonify({"infos": response.infos(question)})
