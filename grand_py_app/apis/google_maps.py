
import requests

from env_variables import MAPS_KEY


class GoogleMaps():

    def __init__(self):
        self.key = MAPS_KEY

    def __request_get(self, address):
        payload = {
            "address" : address,
            "key" : self.key
        }
        request = requests.get(f"https://maps.googleapis.com/maps/api/geocode/json", params=payload)
        return request.json()

    def get_location(self, address):
        data = self.__request_get(address)
        results = data["results"][0]
        geometry = results["geometry"]
        return geometry["location"] # {'lat': 48.8701231, 'lng': 2.3165784}