# https://docs.pytest.org/en/latest/monkeypatch.html
from models.api_googlemaps import GoogleMapsApi
from models.killer_parser import KillerParser


def test_api_googlemaps(monkeypatch):
    """The api_googlemaps test using mocks 'OpenClassrooms'."""

    def mock_geocode(*args, **kwargs):
        """Tips:
        mock_geocode must take as many arguments as the called function
        """

        return {
            "latitude" : 48.856614,
            "longitude": 2.3522219,
            "address"  : "Paris, France"
        }

    monkeypatch.setattr(
        GoogleMapsApi, 'geocoding', mock_geocode)
    api = GoogleMapsApi()
    api_result = api.geocoding("Paris")

    assert api_result["address"]   == "Paris, France"
    assert api_result["latitude"]  == 48.856614
    assert api_result["longitude"] == 2.3522219


# def test_api_mediawiki(monkeypatch):
#     """The api_mediawiki test using mocks."""

#     result = "OpenClassrooms est une école en ligne qui propose à ses membres des cours certifiants et des parcours débouchant sur un métier d'avenir, réalisés en interne, par des écoles, des universités, ou encore par des entreprises partenaires comme Microsoft ou IBM."

#     def mock_summary(*args, **kwargs):
#         return result

#     monkeypatch.setattr(
#         MediawikiApi, 'searching', mock_summary)
#     wikipedia = MediaWikiApi()
#     assert wikipedia.searching('openclassrooms') == result


def test_killer_parser():
    """The parser killer test"""
    sentence = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
    kp = KillerParser()
    request = kp.keep_keywords(sentence)
    assert request == "openclassrooms"
