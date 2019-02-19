# http://py-googlemaps.sourceforge.net/
import googlemaps
from config import GOOGLEMAPS_API_KEY


class GoogleMapsApi:
    """Class to acces API Google Maps.
    """

    def __init__(self):
        self.gmaps = googlemaps.Client(key=GOOGLEMAPS_API_KEY)

    def geocoding(self, address):
        """Geocoding: convert a postal address to latitude and longitude
        
        Arguments:
            address {str} -- a postal adress
        """

        geocode_result = self.gmaps.geocode(address)
        return geocode_result