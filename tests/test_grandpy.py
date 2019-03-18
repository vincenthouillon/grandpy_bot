# https://docs.pytest.org/en/latest/monkeypatch.html
from grandpy.api_googlemaps import GoogleMapsApi
from grandpy.api_mediawiki import MediawikiApi
from grandpy.killer_parser import KillerParser
from grandpy.views import app


def test_api_googlemaps(monkeypatch):
    """The api_googlemaps test using mocks 'OpenClassrooms'."""

    def mock_geocode(*args, **kwargs):
        """Tips:
        mock_geocode must take as many arguments as the called function
        """

        return {
            "latitude": 48.856614,
            "longitude": 2.3522219,
            "address": "Paris, France"
        }

    monkeypatch.setattr(
        GoogleMapsApi, 'geocode', mock_geocode)
    from config import GMAPS_KEY; gmaps_key = GMAPS_KEY
    api = GoogleMapsApi(gmaps_key)
    api_result = api.geocode("Paris")

    assert api_result["address"] == "Paris, France"
    assert api_result["latitude"] == 48.856614
    assert api_result["longitude"] == 2.3522219


def test_api_mediawiki(monkeypatch):
    """The api_mediawiki test using mocks."""

    result = "OpenClassrooms est une école en ligne..."

    def mock_summary(*args, **kwargs):
        return result

    monkeypatch.setattr(
        MediawikiApi, 'search', mock_summary)
    wikipedia = MediawikiApi()
    assert wikipedia.search('openclassrooms') == result


def test_killer_parser():
    """The parser killer test."""
    sentence = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
    address = "7 Cité Paradis, 75010 Paris"
    kp = KillerParser()
    test_sentence = kp.sentence_parser(sentence)
    assert test_sentence == "openclassrooms"
    test_address = kp.address_parser(address)
    assert test_address == "cité paradis paris"
