from flask import Flask
import os

app = Flask(__name__)
if app.config['ENV'] != 'development':
    app.config.from_object('config.DevelopmentConfig')
else:
    app.config['GMAPS_KEY'] = os.environ.get('GMAPS_KEY')


from .views import app
