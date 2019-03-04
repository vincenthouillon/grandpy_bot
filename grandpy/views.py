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


def data_processing():
    user_input = request.args.get('query')
    if user_input:
        keyword: str = parser.keep_keywords(user_input)
        geocode: dict = gmap.geocoding(keyword)
        history: str = wikipedia.searching(keyword)
        address: str = geocode['address']
        latitude: str = geocode['latitude']
        longitude: str = geocode['longitude']
        #! FOR DEBUG
        print("*" * 40)
        print(keyword)
        print(address)
        print(latitude)
        print(longitude)
        print(history)
        print("*" * 40)
    # print(user_input)


@app.route('/')
def index():
    data_processing()
    return render_template('index.html')


@app.route('/get_json')
def get_json():
    """Return data in JSON Format."""
    return jsonify(
        latitude=48.874779,
        longitude=2.350489
    )


if __name__ == '__main__':
    app.run()
