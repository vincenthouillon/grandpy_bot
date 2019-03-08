from flask import Flask, jsonify, render_template, request
from models.api_googlemaps import GoogleMapsApi
from models.api_mediawiki import MediawikiApi
from models.killer_parser import KillerParser
import models.messages as msg

app = Flask(__name__)
gmap = GoogleMapsApi()
parser = KillerParser()
wikipedia = MediawikiApi()

# Config options
app.config.from_object('grandpy.config.settings')
# To get one variable, tape app.config['MY_VARIABLE']


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_json', methods=['POST'])
def get_json():
    """Return data in JSON Format."""
    address_msg = msg.address_msg()
    summary_msg = msg.summary_msg()
    error_msg = msg.error_msg()
    data = request.form['query']
    keyword: str = parser.keep_keywords(data)
    geocode: dict = gmap.geocoding(keyword)
    try:
        history: str = wikipedia.searching(keyword)
        address: str = geocode['address']
        latitude: str = geocode['latitude']
        longitude: str = geocode['longitude']
    except:
        history = None
        address = None
        latitude = None
        longitude = None
    print('OK')

    return jsonify(
        sentence = data,
        address=address,
        longitude=longitude,
        latitude=latitude,
        history=history,
        address_msg = address_msg,
        summary_msg = summary_msg,
        error_msg = error_msg
)


if __name__ == '__main__':
    app.run()

