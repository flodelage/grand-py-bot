
import requests

from env_variables import MAPS_KEY


class GoogleMaps():

    def __init__(self):
        self.key = MAPS_KEY

    def request_get(self, address):
        request = requests.get(f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={self.key}")
        return request.json()