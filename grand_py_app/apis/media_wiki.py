
import requests
import random


class MediaWiki():

    def __request_get(self, location):
        payload = {
            "action": "query",
            "format": "json",
            "generator": "geosearch",
            "ggscoord": f"{location['lat']}|{location['lng']}",
            "ggslimit": "5",
            "ggsradius": "1000",
            "prop" : "extracts",
            "exintro" : "",
            "explaintext" : ""
        }
        request = requests.get("https://fr.wikipedia.org/w/api.php", params=payload)
        return request.json()

    def get_informations(self, location):
        location_infos = {
            "title": "",
            "extract": "",
            "wiki_url": "",
            "response_nb": ""
        }

        data = self.__request_get(location)

        try:
            pages = data["query"]["pages"]
            random_page_id = random.choices(list(pages.keys()))[0]
            random_page = pages[random_page_id]
            location_infos["title"] = random_page['title']
            location_infos["extract"] = random_page['extract']
            location_infos["wiki_url"] = f"https://fr.wikipedia.org/wiki/{random_page['title']}".replace(" ", "_")
            location_infos["response_nb"] = "many" if len(pages) > 1 else "one"
        except KeyError:
            location_infos["response_nb"] = "none"
        return location_infos