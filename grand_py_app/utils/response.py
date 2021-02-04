
from grand_py_app.utils.question_cleaner import QuestionCleaner
from grand_py_app.apis.google_maps import GoogleMaps
from grand_py_app.apis.media_wiki import MediaWiki

class Response:
    def __init__(self):
        self.cleaner = QuestionCleaner()
        self.maps = GoogleMaps()
        self.wiki = MediaWiki()

    def infos(self, user_question):
        infos = {
            'user_question': "",
            'maps_address': "",
            'maps_lat': 0,
            'maps_lng': 0,
            'maps_status': "",
            'wiki_title': "",
            'wiki_extract': "",
            'wiki_url': "",
            'wiki_response_nb': ""
        }

        cleaned_request = self.cleaner.remove_all(user_question)
        location = self.maps.get_location(cleaned_request)
        story = self.wiki.get_story({'lat':location['lat'],'lng':location['lng']})

        infos['user_question'] = user_question.capitalize()
        infos['maps_address'] = location['address']
        infos['maps_lat'] = location['lat']
        infos['maps_lng'] = location['lng']
        infos['maps_status'] = location['status']
        infos['wiki_title'] = story['title']
        infos['wiki_extract'] = story['extract']
        infos['wiki_url'] = story['wiki_url']
        infos['wiki_response_nb'] = story['response_nb']
        return infos