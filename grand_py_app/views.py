
from flask import Flask, render_template, request, jsonify
from form import QuestionForm
from grand_py_app.utils.response import Response


app = Flask(__name__)


@app.route('/')
def home():
    form = QuestionForm()
    return render_template('home.html', form=form)


@app.route('/process', methods=['POST'])
def process():
    question = request.form['question']
    response = Response()
    return jsonify({"infos": response.infos(question)})
