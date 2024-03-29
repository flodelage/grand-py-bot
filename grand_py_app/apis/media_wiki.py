
import requests
import random


class MediaWiki():
    """
    Responsability: Call the Wikipedia's API in order to retrieve a story
    about a place from geographic coordinates
    """

    def request_get(self, location):
        """
        Sends "get request" to the the Wikipedia's API and returns Json data.
        Gives geographic coordinates as main parameter.
        """
        payload = {
            "action": "query",
            "format": "json",
            "generator": "geosearch",
            "ggscoord": f"{location['lat']}|{location['lng']}",
            "ggslimit": "5",
            "ggsradius": "1000",
            "prop": "extracts",
            "exintro": "",
            "explaintext": ""
        }

        request = requests.get("https://fr.wikipedia.org/w/api.php", params=payload)
        return request.json()

    def get_story(self, location):
        """
        Sort infos and returns a random story (if many available) from a json
        """
        data = self.request_get(location)

        location_infos = {
            "title": "",
            "extract": "",
            "wiki_url": "",
            "response_nb": ""
        }

        try:
            # if at least one result is found, the location
            # informations dict is updated
            pages = data["query"]["pages"]
            random_page_id = random.choices(list(pages.keys()))[0]
            random_page = pages[random_page_id]
            location_infos["title"] = random_page['title']
            location_infos["extract"] = random_page['extract']
            location_infos["wiki_url"] = f"https://fr.wikipedia.org/wiki/{random_page['title']}".replace(" ", "_")
            # sets response_nb differently if API finds one or more stories
            location_infos["response_nb"] = "many" if len(pages) > 1 else "one"
        except KeyError:
            # if no result is found by the API
            location_infos["response_nb"] = "none"
        return location_infos
