
from grand_py_app.apis.google_maps import GoogleMaps

class TestGoogleMaps:

    maps = GoogleMaps()

    def test_request_get(self, monkeypatch):
        import grand_py_app.apis.google_maps
        def mock_request_get(self, address):
            return {'results': [{'address_components': [{'long_name': '55', 'short_name': '55', 'types': ['street_number']}, {'long_name': 'Rue du Faubourg Saint-Honoré', 'short_name': 'Rue du Faubourg Saint-Honoré', 'types': ['route']}, {'long_name': 'Paris', 'short_name': 'Paris', 'types': ['locality', 'political']}, {'long_name': 'Département de Paris', 'short_name': 'Département de Paris', 'types': ['administrative_area_level_2', 'political']}, {'long_name': 'Île-de-France', 'short_name': 'IDF', 'types': ['administrative_area_level_1', 'political']}, {'long_name': 'France', 'short_name': 'FR', 'types': ['country', 'political']}, {'long_name': '75008', 'short_name': '75008', 'types': ['postal_code']}], 'formatted_address': '55 Rue du Faubourg Saint-Honoré, 75008 Paris, France', 'geometry': {'bounds': {'northeast': {'lat': 48.8709496, 'lng': 2.3174997}, 'southwest': {'lat': 48.8698034, 'lng': 2.315718}}, 'location': {'lat': 48.8701231, 'lng': 2.3165784}, 'location_type': 'ROOFTOP', 'viewport': {'northeast': {'lat': 48.8717254802915, 'lng': 2.317957830291502}, 'southwest': {'lat': 48.8690275197085, 'lng': 2.315259869708498}}}, 'place_id': 'ChIJi-rDls5v5kcRad3lk5loQiI', 'types': ['premise']}], 'status': 'OK'}

        monkeypatch.setattr(grand_py_app.apis.google_maps, 'request_get', mock_request_get)
        assert {'results': [{'address_components': [{'long_name': '55', 'short_name': '55', 'types': ['street_number']}, {'long_name': 'Rue du Faubourg Saint-Honoré', 'short_name': 'Rue du Faubourg Saint-Honoré', 'types': ['route']}, {'long_name': 'Paris', 'short_name': 'Paris', 'types': ['locality', 'political']}, {'long_name': 'Département de Paris', 'short_name': 'Département de Paris', 'types': ['administrative_area_level_2', 'political']}, {'long_name': 'Île-de-France', 'short_name': 'IDF', 'types': ['administrative_area_level_1', 'political']}, {'long_name': 'France', 'short_name': 'FR', 'types': ['country', 'political']}, {'long_name': '75008', 'short_name': '75008', 'types': ['postal_code']}], 'formatted_address': '55 Rue du Faubourg Saint-Honoré, 75008 Paris, France', 'geometry': {'bounds': {'northeast': {'lat': 48.8709496, 'lng': 2.3174997}, 'southwest': {'lat': 48.8698034, 'lng': 2.315718}}, 'location': {'lat': 48.8701231, 'lng': 2.3165784}, 'location_type': 'ROOFTOP', 'viewport': {'northeast': {'lat': 48.8717254802915, 'lng': 2.317957830291502}, 'southwest': {'lat': 48.8690275197085, 'lng': 2.315259869708498}}}, 'place_id': 'ChIJi-rDls5v5kcRad3lk5loQiI', 'types': ['premise']}], 'status': 'OK'}
