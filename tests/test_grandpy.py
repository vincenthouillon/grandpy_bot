# https://docs.pytest.org/en/latest/monkeypatch.html
from models.api_googlemaps import GoogleMapsApi


def test_api_googlemaps(monkeypatch):
    """ api_googlemaps test using mocks 'OpenClassrooms' """

    result = (48.87473, 2.3483577)

    def mock_geocode(latitude, longitude):
        return result

    monkeypatch.setattr(
        'models.api_googlemaps.GoogleMapsApi.geocoding', mock_geocode)
    api = GoogleMapsApi()
    assert api.geocoding('openclassrooms') == result


def test_api_mediawiki(monkeypatch):
    """ api_mediawiki test using mocks """

    result = "OpenClassrooms est une école en ligne qui propose à ses membres des cours certifiants et des parcours débouchant sur un métier d'avenir, réalisés en interne, par des écoles, des universités, ou encore par des entreprises partenaires comme Microsoft ou IBM."

    def mock_summary(summary):
        return result

    monkeypatch.setattr(
        'models.api_mediawiki.MediawikiApi.searching', mock_summary)
    wikipedia = MediaWikiApi()
    assert wikipedia.searching('openclassrooms') == result


def test_killer_parser():
    """parser killer test """

    request = KillerParser.keep_keywords(
        "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
    )
    assert request == "openclassrooms"
