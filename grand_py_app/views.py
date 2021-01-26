
from flask import Flask, render_template, request, jsonify
from grand_py_app.utils.question_cleaner import QuestionCleaner
from grand_py_app.apis.google_maps import GoogleMaps
from grand_py_app.apis.media_wiki import MediaWiki


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/process', methods=['POST'])
def process():
    question = request.form['question']
    cleaner = QuestionCleaner()
    maps = GoogleMaps()
    wiki = MediaWiki()
    address = cleaner.remove_all(question)
    location = maps.get_location(address)
    location_coordinates = {'lat':location['lat'],'lng':location['lng']}
    return jsonify({"address": location['address'],
                    "location_coordinates": location_coordinates,
                    "location_infos": wiki.get_informations(location_coordinates)})
