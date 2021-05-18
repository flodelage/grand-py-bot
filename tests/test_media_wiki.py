
from grand_py_app.apis.media_wiki import MediaWiki


def test_get_story(monkeypatch):
    def mock_request_get(self, location):
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
        'grand_py_app.apis.media_wiki.MediaWiki.request_get', mock_request_get
    )

    wiki = MediaWiki()
    location = "Tour Eiffel"
    expected_result = {
        'title': 'Îles Gili',
        'extract':
            "Les îles Gili, Gili Islands en anglais, est un terme qui désigne trois petites îles d'Indonésie "
            "situées au large de la côte nord-ouest de l'île de Lombok : Air, Meno et Trawangan. Cette appellation "
            "est un abus de langage, puisque gili veut dire « île » en sasak, la langue de la majorité des habitants de Lombok. "
            "Toutes les îles qui entourent Lombok portent d'ailleurs un nom précédé de gili, par exemple Gili Nanggu, située au sud-ouest de Lombok."
            "\nLa plus grande est Trawangan avec 2kmX1km, la plus petite est Gili Meno.\n"
            "Les trois iles étaient sans habitants permanents avant le développement du tourisme à la fin des années 80 - début 90."
            "\nAdministrativement, les îles font partie du kabupaten de Lombok occidental dans la province des petites îles de la Sonde occidentales.",
        'wiki_url': 'https://fr.wikipedia.org/wiki/Îles_Gili',
        'response_nb': 'one'
    }

    assert wiki.get_story(location) == expected_result
