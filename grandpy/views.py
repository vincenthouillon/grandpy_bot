from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Config options
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_json')
def get_json():
    """Return data in JSON Format."""
    return jsonify(
        latitude  = 48.874779,
        longitude = 2.350489
    )

if __name__ == '__main__':
    app.run()
