from flask import Flask, jsonify, render_template, request
from models.api_googlemaps import GoogleMapsApi
from models.api_mediawiki import MediawikiApi
from models.killer_parser import KillerParser

app = Flask(__name__)
gmap = GoogleMapsApi()
parser = KillerParser()
wikipedia = MediawikiApi()

# Config options
app.config.from_object('grandpy.config.settings')
# To get one variable, tape app.config['MY_VARIABLE']


@app.route('/')
def index():
    global query 
    query = request.args.get('query')

    return render_template('index.html')


@app.route('/get_json')
def get_json():
    """Return data in JSON Format."""
    if query != None:
        sentence = query
        keyword: str = parser.keep_keywords(sentence)
        # geocode: dict = gmap.geocoding(keyword)
        history: str = wikipedia.searching(keyword)
        # address: str = geocode['address']
        # latitude: str = geocode['latitude']
        # longitude: str = geocode['longitude']

        return jsonify(
            keyword=sentence,
            # address=address,
            # longitude=longitude,
            # latitude=latitude,
            history=history
        )
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run()
