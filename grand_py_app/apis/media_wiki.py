
import requests


class MediaWiki():

    def __request_get(self, location):
        payload = {
            "action": "query",
            "format": "json",
            "generator": "geosearch",
            "ggscoord": f"{location['lat']}|{location['lng']}",
            "ggslimit": "1",
            "ggsradius": "1000",
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
            "title": "",
            "extract": "",
            "wiki_url": ""
        }

        location_infos["title"] = first_page['title'],
        location_infos["extract"] = first_page['extract'],
        location_infos["wiki_url"] = f"https://fr.wikipedia.org/wiki/{first_page['title']}".replace(" ", "_")
        return location_infos