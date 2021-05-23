
from grand_py_app.utils.response import Response


def test_response(monkeypatch):
    def mock_maps_request_get(self, address):
        return {
            'results': [{
                    'address_components': [
                        {'long_name': 'Gili Islands', 'short_name': 'Gili Islands', 'types': ['archipelago', 'establishment', 'natural_feature']},
                        {'long_name': 'Gili Indah', 'short_name': 'Gili Indah', 'types': ['administrative_area_level_4', 'political']},
                        {'long_name': 'Pemenang', 'short_name': 'Pemenang', 'types': ['administrative_area_level_3', 'political']},
                        {'long_name': 'North Lombok Regency', 'short_name': 'North Lombok Regency', 'types': ['administrative_area_level_2', 'political']},
                        {'long_name': 'West Nusa Tenggara', 'short_name': 'West Nusa Tenggara', 'types': ['administrative_area_level_1', 'political']},
                        {'long_name': 'Indonesia', 'short_name': 'ID', 'types': ['country', 'political']}
                    ],
                    'formatted_address': 'Gili Islands, Gili Indah, Pemenang, North Lombok Regency, West Nusa Tenggara, Indonesia',
                    'geometry': {
                        'bounds': {'northeast': {'lat': -8.3355706, 'lng': 116.0886704}, 'southwest': {'lat': -8.3681175, 'lng': 116.023656}},
                        'location': {'lat': -8.351844, 'lng': 116.0561632},
                        'location_type': 'APPROXIMATE',
                        'viewport': {'northeast': {'lat': -8.3355706, 'lng': 116.0886704}, 'southwest': {'lat': -8.3681175, 'lng': 116.023656}}
                    },
                    'place_id': 'ChIJi-ChIJPfMXq1zHli0RPkN9ctDc3D8', 'types': ['archipelago', 'establishment', 'natural_feature']
            }], 'status': 'OK'
        }

    def mock_wiki_request_get(self, location):
        return {
            'batchcomplete': '', 'query': {
                'pages': {
                    '1426766': {
                        'pageid': 1426766,
                        'ns': 0,
                        'title': 'Îles Gili',
                        'index': -1,
                        'extract':
                            "Les îles Gili, Gili Islands en anglais, est un terme qui désigne trois petites îles d'Indonésie "
                            "situées au large de la côte nord-ouest de l'île de Lombok : Air, Meno et Trawangan. Cette appellation "
                            "est un abus de langage, puisque gili veut dire « île » en sasak, la langue de la majorité des habitants de Lombok. "
                            "Toutes les îles qui entourent Lombok portent d'ailleurs un nom précédé de gili, par exemple Gili Nanggu, située au sud-ouest de Lombok."
                            "\nLa plus grande est Trawangan avec 2kmX1km, la plus petite est Gili Meno.\n"
                            "Les trois iles étaient sans habitants permanents avant le développement du tourisme à la fin des années 80 - début 90."
                            "\nAdministrativement, les îles font partie du kabupaten de Lombok occidental dans la province des petites îles de la Sonde occidentales."
                    }
                }
            }
        }

    monkeypatch.setattr(
        'grand_py_app.apis.google_maps.GoogleMaps.request_get', mock_maps_request_get
    )

    monkeypatch.setattr(
        'grand_py_app.apis.media_wiki.MediaWiki.request_get', mock_wiki_request_get
    )

    response = Response()
    user_question = "Salut GrandPy ! Tu vas bien ? Tu connais Gili Air ?"
    expected_result = {'user_question': 'Salut grandpy ! tu vas bien ? tu connais gili air ?',
                       'maps_address': 'Gili Islands, Gili Indah, Pemenang, North Lombok Regency, West Nusa Tenggara, Indonesia',
                       'maps_lat': -8.351844,
                       'maps_lng': 116.0561632,
                       'maps_status': 'approximate',
                       'wiki_title': 'Îles Gili',
                       'wiki_extract':
                            "Les îles Gili, Gili Islands en anglais, est un terme qui désigne trois petites îles d'Indonésie "
                            "situées au large de la côte nord-ouest de l'île de Lombok : Air, Meno et Trawangan. Cette appellation "
                            "est un abus de langage, puisque gili veut dire « île » en sasak, la langue de la majorité des habitants de Lombok. "
                            "Toutes les îles qui entourent Lombok portent d'ailleurs un nom précédé de gili, par exemple Gili Nanggu, située au sud-ouest de Lombok."
                            "\nLa plus grande est Trawangan avec 2kmX1km, la plus petite est Gili Meno.\n"
                            "Les trois iles étaient sans habitants permanents avant le développement du tourisme à la fin des années 80 - début 90."
                            "\nAdministrativement, les îles font partie du kabupaten de Lombok occidental dans la province des petites îles de la Sonde occidentales.",
                       'wiki_url': 'https://fr.wikipedia.org/wiki/Îles_Gili',
                       'wiki_response_nb': 'one'}
    assert response.infos(user_question) == expected_result
