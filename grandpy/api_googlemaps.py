# http://py-googlemaps.sourceforge.net/
import googlemaps


class GoogleMapsApi:
    """Class to acces API Google Maps.

    Example:
        address = "OpenClassrooms"
        gm = GoogleMapsApi()
        print(gm.geocode(address))
    Return a dictionary:
        {'address': '7 Cité Paradis, 75010 Paris, France', 'latitude': 48.8747265, 'longitude': 2.3505517}
    """

    def __init__(self, api_key):
        self.gmaps = googlemaps.Client(key=api_key)

    def geocode(self, address):
        """Geocoding: convert a postal address to latitude and longitude

        Arguments:
            address {str} -- a postal adress
        """

        geocode_result = self.gmaps.geocode(address, region='fr')

        try:
            address = geocode_result[0]["formatted_address"]
            lat = geocode_result[0]["geometry"]["location"]["lat"]
            lng = geocode_result[0]["geometry"]["location"]["lng"]

            return {
                "address": address,
                "latitude": lat,
                "longitude": lng
            }
        except IndexError:
            return "no result"
