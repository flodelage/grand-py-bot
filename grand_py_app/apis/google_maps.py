
import googlemaps

from env_variables import MAPS_KEY

# gmaps = googlemaps.Client(key=MAPS_KEY)
# geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

class GoogleMaps(googlemaps.Client(key=MAPS_KEY)):

    def search_address(self, address):
        return self.geocode(address)
