
from config import MAPS_GEOCODING_KEY
import requests


"""
Responsability: Call the Google's API in order to retrieve address
and geographic coordinates from the place requested by the user
"""
class GoogleMaps():

    def __init__(self):
        self.key = MAPS_GEOCODING_KEY

    def request_get(self, address):
        """
        Sends "get request" to the the Google Maps'API and returns Json data.
        Gives a place or an address as parameters.
        """
        address_splited = address.split() # ['55', 'rue', 'faubourg', 'saint', 'honoré', 'paris']
        address_for_url = "+".join(address_splited) # '55+rue+faubourg+saint+honoré+paris'

        payload = {
            "address" : address_for_url,
            "key" : self.key
        }

        request = requests.get(f"https://maps.googleapis.com/maps/api/geocode/json", params=payload)
        return request.json()

    def get_location(self, address):
        """
        Sort and get the necessary infos (address, geographic coordinates, status) from a json element
        """
        data = self.request_get(address)  # Call the API and store Json data

        location = {
            'address': "",
            'lat': 0,
            'lng': 0,
            'status': ""
        }

        try:
            result = data["results"][0]
            # if a result is found, the location dict is updated
            location["address"] = result["formatted_address"]
            location["lat"] = result["geometry"]["location"]["lat"]
            location["lng"] = result["geometry"]["location"]["lng"]
            if result["geometry"]["location_type"] != "APPROXIMATE":
                # if the API returns an exact geographic coordinates
                location["status"] = "accurate"
            else:
                # if the API returns an approximate geographic coordinates
                location["status"] = "approximate"
        except IndexError:
            # if no result is found by the API
            location["status"] = "not_found"
        return location
