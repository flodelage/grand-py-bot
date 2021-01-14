
import requests


class MediaWiki():

    def __request_get(self, location):
        payload = {
            "action": "query",
            "format": "json",
            "generator": "geosearch",
            "ggscoord": f"{location['lat']}|{location['lng']}",
            "ggslimit": "10",
            "ggsradius": "100",
            "prop" : "extracts",
            "exintro" : "",
            "explaintext" : ""
        }
        request = requests.get("https://fr.wikipedia.org/w/api.php", params=payload)
        return request.json()

        def get_informations(self, location):
            data = self.__request_get(location)
            pages = data["query"]["pages"]
            first_page = pages[list(pages)[0]]
            location_infos = {
                "title": first_page['title'],
                "extract": first_page['extract']
                "wiki_url": "https://fr.wikipedia.org/"
            }
            return location_infos