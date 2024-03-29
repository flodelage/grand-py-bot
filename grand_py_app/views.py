
from flask import Flask, render_template, request, jsonify
from grand_py_app.form import QuestionForm
from grand_py_app.utils.response import Response


app = Flask(__name__)


@app.route('/')
def home():
    form = QuestionForm()
    return render_template('home.html', form=form)


@app.route('/process', methods=['POST'])
def process():
    """
    Retrieves and processes user input in order to
    provide the necessary elements to the front
    """
    question = request.form['question']
    response = Response()
    return jsonify({"infos": response.infos(question)})
