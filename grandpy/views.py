from flask import Flask, jsonify, render_template, request

import models.messages as msg
from grandpy.config.settings import GOOGLEMAPS_API_KEY
from models.api_googlemaps import GoogleMapsApi
from models.api_mediawiki import MediawikiApi
from models.killer_parser import KillerParser

app = Flask(__name__)
gmap = GoogleMapsApi(GOOGLEMAPS_API_KEY)
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
    sentence = request.form['query']
    keyword: str = parser.sentence_parser(sentence)
    geocode: dict = gmap.geocoding(keyword)
    try:
        wiki_fetch = parser.sentence_address(geocode['address'])
        wiki: str = wikipedia.searching(wiki_fetch)
        wiki_resume: str = wiki[0]
        wiki_url:str = wiki[1]
        address: str = geocode['address']
        latitude: str = geocode['latitude']
        longitude: str = geocode['longitude']
    except:
        wiki_resume = wiki_url = address = latitude = longitude = None
        print('Receipt of data: failed')
    print('Receipt of data: OK')

    return jsonify(
        sentence=sentence,
        address=address,
        longitude=longitude,
        latitude=latitude,
        history=wiki_resume,
        wikilink=wiki_url,
        address_msg=msg.address_msg(),
        summary_msg=msg.summary_msg(),
        error_msg=msg.error_msg()
    )


if __name__ == '__main__':
    app.run()
