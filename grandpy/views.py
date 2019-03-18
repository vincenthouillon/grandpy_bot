import os

from flask import Flask, jsonify, render_template, request

import grandpy.messages as msg
from grandpy.api_googlemaps import GoogleMapsApi
from grandpy.api_mediawiki import MediawikiApi
from grandpy.killer_parser import KillerParser

app = Flask(__name__)
try:
    app.config.from_object('config')
    GMAPS_KEY = app.config['GMAPS_KEY']
except:
    GMAPS_KEY = os.environ.get('GMAPS_KEY')

gmaps = GoogleMapsApi(GMAPS_KEY)
parser = KillerParser()
wikipedia = MediawikiApi()


@app.route('/')
def index():
    return render_template('index.html', gmaps_key = GMAPS_KEY)


@app.route('/process', methods=['POST'])
def process():
    """Return data in JSON Format."""
    sentence = request.form['query']
    keyword: str = parser.sentence_parser(sentence)
    geocode: dict = gmaps.geocode(keyword)
    try:
        wiki_fetch = parser.address_parser(geocode['address'])
        wiki: str = wikipedia.search(wiki_fetch)
        wiki_resume: str = wiki[0]
        wiki_url: str = wiki[1]
        address: str = geocode['address']
        latitude: str = geocode['latitude']
        longitude: str = geocode['longitude']
    except:
        wiki_resume = wiki_url = address = latitude = longitude = None

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
