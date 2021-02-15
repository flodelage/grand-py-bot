
import requests

# from env_variables import MAPS_KEY


class GoogleMaps():

    def __init__(self):
        # self.key = MAPS_KEY
        self.key = "AIzaSyAltnzowbiyt85fq95bSJEZXcg93hgR8vA"

    def request_get(self, address):
        address_splited = address.split() # ['55', 'rue', 'faubourg', 'saint', 'honoré', 'paris']
        address_for_url = "+".join(address_splited) # '55+rue+faubourg+saint+honoré+paris'

        payload = {
            "address" : address_for_url,
            "key" : self.key
        }

        request = requests.get(f"https://maps.googleapis.com/maps/api/geocode/json", params=payload)
        return request.json()

    def get_location(self, address):
        location = {
            'address': "",
            'lat': 0,
            'lng': 0,
            'status': ""
        }

        data = self.request_get(address)
        try:
            result = data["results"][0]
            location["address"] = result["formatted_address"]
            location["lat"] = result["geometry"]["location"]["lat"]
            location["lng"] = result["geometry"]["location"]["lng"]
            if result["geometry"]["location_type"] != "APPROXIMATE":
                location["status"] = "accurate"
            else:
                location["status"] = "approximate"
        except IndexError:
            location["status"] = "not_found"
        return location
